"""
Complete reproduction of Iris experiment from Paper Section 4.1
严格按照论文Section 4.1和图17的完整流程
关键修正：使用属性级m(Φ)平均值判断FOD完整性
"""

import numpy as np
from sklearn.datasets import load_iris
from fuzzy_gap_statistic import FuzzyGapStatistic


def example_iris_incomplete_fod():
    """
    Example: Iris dataset with incomplete FOD
    完全复现论文 Section 4.1
    """
    print("=" * 70)
    print("Reproducing Paper Section 4.1: Iris Dataset Experiment")
    print("Following Fig.17 Strategy with Corrected m(Φ) Calculation")
    print("=" * 70)

    # Load Iris data
    iris = load_iris()
    data = iris.data
    target = iris.target
    target_names = iris.target_names

    print(f"\nDataset Info:")
    print(f"  Total samples: {data.shape[0]}")
    print(f"  Features: {data.shape[1]} (SL, SW, PL, PW)")
    print(f"  Classes: {list(target_names)}")

    # 论文设定：FOD = {setosa, virginica}，即已知类别为 0 和 2
    known_classes = [0, 2]  # setosa, virginica
    unknown_classes = [1]   # versicolor

    n_known = len(known_classes)

    print(f"\nExperiment Setup (Ω₁ = {{setosa, virginica}}):")
    print(f"  Known classes: {[target_names[i] for i in known_classes]}")
    print(f"  Unknown classes: {[target_names[i] for i in unknown_classes]}")

    # ===== 数据划分：严格按照论文Section 4.1 =====
    print("\n" + "=" * 70)
    print("Data Split (following paper Section 4.1)")
    print("=" * 70)

    np.random.seed(42)

    train_indices = []
    test_indices = []

    # 论文方法：
    # (1) setosa和virginica各选40个作为训练集（建立命题表示模型）
    # (2) versicolor选30个 + setosa和virginica各剩余10个 = 50个测试集

    for cls in range(3):
        cls_indices = np.where(target == cls)[0]
        np.random.shuffle(cls_indices)

        if cls in known_classes:
            # setosa (0) 和 virginica (2): 40个训练，10个测试
            train_indices.extend(cls_indices[:40])
            test_indices.extend(cls_indices[40:])
        else:
            # versicolor (1): 0个训练，30个测试
            test_indices.extend(cls_indices[:30])

    # 提取数据
    train_data = data[train_indices]
    train_labels = target[train_indices]
    test_data = data[test_indices]
    test_labels = target[test_indices]

    print(f"\nData split:")
    print(f"  Training set: {train_data.shape[0]} samples (用于建立TFN模型)")
    for cls in known_classes:
        n_cls = np.sum(train_labels == cls)
        print(f"    - {target_names[cls]}: {n_cls} samples")

    print(f"  Test set: {test_data.shape[0]} samples (用于鉴别生成GBPA)")
    for cls in range(3):
        n_cls = np.sum(test_labels == cls)
        if n_cls > 0:
            print(f"    - {target_names[cls]}: {n_cls} samples")

    # ===== 运行Fuzzy Gap Statistic =====
    print("\n" + "=" * 70)
    print("Running Fuzzy Gap Statistic Algorithm (Fig.17 Strategy)")
    print("Key Correction: Using attribute-level average m(Φ) for FOD judgment")
    print("=" * 70)

    fgs = FuzzyGapStatistic(critical_value=0.5, max_iterations=100)

    results = fgs.fit(
        test_data=test_data,
        train_data=train_data,
        train_labels=train_labels,
        n_known_targets=n_known,
        max_clusters=6
    )

    # ===== 结果总结 =====
    print("\n" + "=" * 70)
    print("FINAL RESULTS")
    print("=" * 70)

    print(f"\nStep 1 Results:")
    print(f"  m̄(∅) (attribute-level average) = {results['m_empty_mean']:.4f}")
    print(f"  Expected value from paper (Table 2): 0.589")
    print(f"  Difference: {abs(results['m_empty_mean'] - 0.589):.4f}")
    print(f"  Critical value p = 0.5")
    print(f"  System State: {results['diagnosis']['state']}")
    print(f"  FOD Complete: {results['fod_is_complete']}")

    if not results['fod_is_complete']:
        print(f"\nStep 2 Results:")
        print(f"  Optimal k = {results.get('optimal_k', 'N/A')}")
        print(f"  Expected value from paper (Fig. 4): k=3")

        print(f"\nStep 3 Results:")
        print(f"  Known targets: {n_known}")
        print(f"  Unknown targets: {results.get('n_unknown_targets', 0)}")
        print(f"  Total targets: {results.get('total_targets', n_known)}")

        print(f"\n--- Verification ---")
        actual_classes = len(np.unique(test_labels))
        predicted_classes = results.get('total_targets', n_known)
        print(f"  Actual classes in test set: {actual_classes}")
        print(f"  Predicted total classes: {predicted_classes}")

        if predicted_classes == actual_classes:
            print(f"  ✓ CORRECT: Successfully detected {predicted_classes - n_known} unknown class(es)!")
        else:
            print(f"  ✗ INCORRECT: Predicted {predicted_classes} but actual is {actual_classes}")

    print("\n" + "=" * 70)
    print("Experiment Completed Successfully!")
    print("=" * 70)

    return results


if __name__ == "__main__":
    results = example_iris_incomplete_fod()
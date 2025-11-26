# Determine the number of unknown targets in Open World based on Elbow method

Fan Liu, Yong Deng

Abstract-Generalized evidence theory (GET) as an extension of Dempster-Shafer (D-S) evidence theory can deal with uncertain information fusion in open world. However, one of the open issues is to detect the number of unknown targets. In this paper, a new method based on Elbow method is proposed to solve this problem. After the identification of the open world, K-means clustering is used to cluster categories. Then, Elbow method is used to find a correct number of unknown targets. The frame of discernment is reupdated. To test effectiveness of proposed method, several experiments are conducted. The results illustrate the advantage of the proposed method in open world.

Index Terms-Dempster-Shafer Evidence Theory, Generalized Evidence Theory, Open world, Fuzzy sets, K-means, Elbow Method.

## I. INTRODUCTION

Dempster-Shafer (D-S) evidence theory [1], [2], is an effective tool to deal with uncertainty [3], [4] in many fields, such as information fusion [5], [6], [7], [8], data classification [9], uncertainty [10], [11], [12], [13], [14], complex networks [15], fuzzy systems [16], [17], [18], [19], [20], [21], machine learning [22], [23], [24], [25] and decision making [26], [27], [28], [29], [30]. One of the open issues of evidence theory is to handle highly conflicting evidence [31], [32].

Many researchers proposed a lot of conflict management methods which can be mainly divided into two types: modifying combination rule [33], [34], [35] and modifying data models [36]. However, the evidence for conflict lacks systematic and comprehensive analyses. Recently, a new theory called Generalized Evidence Theory (GET) was proposed [37]. GET as the extension of evidence theory can summarize the evidence conflict into two aspects: one is the interference or the unreliability of the sensor, and another is the incomplete understanding of the knowledge in open world.

To the problem of incomplete frame of discernment, Jiang et al. [38] proposed a method to solve this problem by determining the size of the generalized basic probability assessment assigned to the empty set and compared it to the threshold. However, one of the problems is that this method can only judge whether the frame of discernment is complete or not, but cannot determine the number of targets in open world. It is necessary to solve this problem.

The motivation of this paper is to find a more general method to solve conflict management, when the frame of discernment is incomplete. Firstly, conflict management has always been a open issue in D-S theory. Incomplete frame of discernment and disturbed sensors are the two main reasons leading to conflict. In order to better handle the fusion of conflicting evidence, it is very necessary to identify whether the framework is complete or not. The generalized evidence theory (GET) is an innovative theory that can represent and process uncertain information in an incomplete framework of discernment. In GET, the empty set is considered to be a focal element of the same property as other elements and represents the unknown. For instance, assuming that the framework of discernment has three targets \( (a, b \) , and c), the sensors can only recognize the difference among the three targets. If a new target \( d \) appears, the sensors cannot distinguish which of the previous three targets. In GET, the empty set can be interpreted as unknown targets. However, when there are more than one unknown targets, how to identify the number of unknown targets is a key issue.

The contribution of this paper is as follows. First, to the best our knowledge, this is the first attempt to propose this problem in GET. Second, to solve this problem, a new method will be proposed. Determine the number of unknown targets in open world based on Elbow method, when the frame of discernment is incomplete. Using K-means clustering recognizes the number of elements in open world. Then, Elbow method is used to find an optimal number of elements and re-update frame of discernment. Finally, we also set up an innovative experiment to verify the proposed method.

The rest of this paper is organized as follows. Section 2 introduces some basic preliminaries. Proposed method is presented in Section 3. Several experiments are conducted to show the effectiveness of the proposed method in Section 4. Finally, conclusion is given in Section 5.

## II. Preliminaries

In this section, some preliminaries, including Generalized Evidence Theory [37], K-means Clustering [39] and Elbow method [40], are briefly introduced.

---

The work is partially supported by National Natural Science Foundation of China (Grant No.61973332). (Corresponding author: Yong Deng)

Fan Liu is with Institute of Fundamental and Frontier Science & Yingcai Honors of school & School of Mathematical Sciences, University of Electronic Science and Technology of China, Chengdu, 610054, China.

Yong Deng is with Institute of Fundamental and Frontier Science, University of Electronic Science and Technology of China, Chengdu, 610054, China (E-mail: dengentropy@uestc.edu.cn, prof.deng@hotmail.com).

---

## A. Generalized evidence theory

Generalized evidence theory is the extension of Dempster-Shafer evidence theory which can deal with many issues [41], [42], [43], [44], [45] under open world [37]. The uncertainty information processing based on evidence theory in open world has been paid attention recently [46], [47], [48], [49]. Here some basic definitions are given.

Let \( \Omega \) be a countable set of \( n \) elements called the frame of discernment in an open world which denotes a finite nonempty set of mutually exclusive and exhaustive hypotheses. Assume that it contains \( \Omega  = \left\{  {{A}_{1},{A}_{2},{A}_{3},\cdots ,{A}_{n}}\right\}  .P\left( \Omega \right) \) is the power set containing all the possible subsets of it. It is composed of \( {2}^{n} \) elements of \( P\left( \Omega \right) \) . Each element of \( {2}^{n} \) represents a proposition.

Definition 1. A Generalized basic probability assignment (GBPA) is a function. The range is from \( P\left( \Omega \right) \) to \( \left\lbrack  {0,1}\right\rbrack \) , which is defined by [37]

\[
m : P\left( \Omega \right)  \mapsto  \left\lbrack  {0,1}\right\rbrack \tag{1}
\]

and it should satisfy the following conditions:

\[
\mathop{\sum }\limits_{{A \in  P\left( \Omega \right) }}m\left( A\right)  = 1 \tag{2}
\]

Note that \( m\left( \phi \right)  = 0 \) is not necessary in GET, which is different from Dempster-Shafer(D-S) evidence theory in many fields [50], [51], [52].

Definition 2. Assume two GBPAs: \( {m}_{1}\left( A\right) \) and \( {m}_{2}\left( B\right) \) , the GET combination rule is defined as follows [37].

\[
m\left( A\right)  = \frac{\left( {1 - m\left( \phi \right) }\right) \mathop{\sum }\limits_{{B \cap  C = A}}{m}_{1}\left( B\right) {m}_{2}\left( C\right) }{1 - K} \tag{3}
\]

with

\[
K = \mathop{\sum }\limits_{{B \cap  C = \phi }}{m}_{1}\left( B\right) {m}_{2}\left( C\right) \tag{4}
\]

\[
m\left( \phi \right)  = {m}_{1}\left( \phi \right) {m}_{2}\left( \phi \right) \tag{5}
\]

\[
m\left( \phi \right)  = 1\;\text{ if and only if }\;K = 1 \tag{6}
\]

where the \( K \) is the degree of conflict of evidence. when \( m\left( \phi \right)  = 0 \) , the GET generates to the Dempster-Shafer evidence theory.

Definition 3 Suppose \( m \) is a GBPA that frame of discernment \( \omega \) , where pignistic probability transformation (PPT) is defined as follows [53].

\[
{PPT}\left( \omega \right)  = \mathop{\sum }\limits_{{A \subseteq  P\left( \omega \right) ,\omega  \in  A}}\frac{1}{\left| A\right| }\frac{m\left( A\right) }{1 - m\left( \phi \right) } \tag{7}
\]

## B. K-Means Clustering

K-means clustering is a kind of unsupervised learning method and can help find category in data, which is a vector quantization method [54]. The purpose of K-means clustering is to divide \( n \) observations into \( K \) clusters, each of which belongs to the clustering with the nearest mean, as the prototype of clustering. This leads to data space divided into Voronoi units.

The complete K-means clustering is embodied in Algorithm 1.

Algorithm 1 K-Means

---

Input: The number of clusters \( K \) and database containing

	\( n \) objects.

Output: \( K \) clusters minimize the squared error criterion.

	An initial clustering center is determined for each clus-

	ter.

	The sample set is allocated to nearest neighbor cluster-

	ing according to the principle of minimum distance.

	Using the mean of each cluster as a new clustering

	center.

	Repeat step 2 and 3 until the cluster center is no longer

	changing.

---

## C. Elbow method

Elbow method [40] is proposed to explain and verify the consistency of clustering analysis, aiming to help find the appropriate number of clusters in the data set.

The core idea is to set up the cost function.

\[
J = \mathop{\sum }\limits_{{i = 1}}^{k}\mathop{\sum }\limits_{{x \in  {C}_{i}}}{\left| x - {C}_{i}\right| }^{2} \tag{8}
\]

where \( J \) is the cost function, \( x \) is the element of cluster \( {C}_{i} \) and \( k \) is the number of clusters \( \left| {C}_{i}\right| \) . With the increase of clustering number \( k \) , the sample partition will be more refined. The degree of each cluster will gradually increase, so the cost function \( J \) will naturally become smaller.

When \( k \) is less than the true clustering number, the decrease of \( J \) will be large because the increase of \( k \) will greatly increase the clustering degree of each cluster, and when \( k \) reaches the true clustering number, the return of clustering degree will be rapidly reduced by increasing \( k \) . So the decrease of \( J \) will be sharply reduced, and then it will become flat with the increase of \( J \) value. That is to say, the relation graph of \( J \) and \( k \) is the shape of an elbow, and the corresponding \( k \) value of this elbow is viewed as the real clustering number of the data.

## III. Proposed METHOD

The proposed method is mainly divided into two steps. The first step is to identify whether the identification framework is complete or not. If the frame of discernment is incomplete, the number of targets is re-determined by K-means, and then the correct target number is determined by Elbow method. Finally, the frame of discernment is updated. The flow chart of the proposed method is shown in Fig. 1.

## A. Step 1

How to generate BPA in evidence theory is an open issue. For GET, a method to generate GBPA is presented [55], which is briefly introduced as follows.

Step 1.1: The value of the test sample attribute \( {x}_{i}^{j} \; \left( {i = 1,2,3\ldots , n.j = 1,2,3\ldots , m}\right) \) where \( n \) is the number of samples and \( m \) is the number of attributes, which is used to create a fuzzy triangle number to generate the GBPA. Vertical curve over sample values intersect with fuzzy triangle curves of all categories \( {C}_{i}\left( {i = 1,2,3\ldots , K}\right) \) , where \( K \) is the number of class. Therefore, \( K \) intersections are available. The intersection value is expressed as \( {f}_{i}\left( {i = 1,2,3\ldots n}\right) \) .

![bo_d4hrgfjef24c739bj2p0_2_215_248_668_843_0.jpg](images/bo_d4hrgfjef24c739bj2p0_2_215_248_668_843_0.jpg)

Fig. 1: Flow chart of the proposed method:The proposed method is always divided into two steps. The first step is to establish an initial framework of discernment. Then generate a GPA to determine if the recognition framework is complete. In the second step, the optimal number of targets is found by clustering, and then the framework of discernment is updated.

Step 1.2: The values corresponding to the attribute \( {x}_{i}^{j} \) are sorted in descending order, and the order is expressed as \( {w}_{i} \; \left( {i = 1,2,3\ldots m}\right) \) . The fuzzy triangle curve corresponding to \( {w}_{i} \) is represented by \( {\operatorname{Cur}}_{ij} \) .

Step 1.3: Match test samples and triangular fuzzy number models to generate membership degrees.

Suppose \( A \) is a proposition under the identification framework, and \( t \) is the eigenvalue of the test sample on a certain attribute. The degree of matching between the test sample and the proposition \( A \) is shown as follows.

\[
f\left( {A \leftarrow  t}\right)  = {\left. {u}_{A}\left( x\right) \right| }_{x = t} \tag{9}
\]

Where \( f\left( {A \leftarrow  t}\right) \) is the fuzzy trigonometric function and \( {\left. {u}_{A}\left( x\right) \right| }_{x = t} \) is the value of the membership of the test data belonging to proposition \( A \) .

For a framework of discernment with \( m \) propositions, the way to generate membership is as follows.

\[
f\left( {A}_{1}\right)  = {w}_{1}
\]

\[
f\left( {{A}_{1},{A}_{2}}\right)  = {w}_{2} \tag{10}
\]

\[
\text{ ... }
\]

\[
f\left( {{A}_{1},{A}_{2},{A}_{3},\ldots ,{A}_{m}}\right)  = {w}_{m}
\]

For example, assuming that a framework of discernment has three propositions \( X = \{ S, E, V\} \) , the degree of matching between the test sample \( t \) and the proposition \( \{ S\} ,\{ S, V\} \) , \( \{ S\} ,\{ S, V, E\} \) is as follows.

\[
f\left( {S \leftarrow  t}\right)  = {\left. {u}_{S}\left( x\right) \right| }_{x = t} = {w}_{1}
\]

\[
f\left( {{SV} \leftarrow  t}\right)  = {\left. {u}_{SV}\left( x\right) \right| }_{x = t} = {w}_{2} \tag{11}
\]

\[
{\left. f\left( SVE \leftarrow  t\right)  = {u}_{SVE}\left( x\right) \right| }_{x = t} = {w}_{3}
\]

Step 1.4: Generate GBPA.

The rules for generating GBPA are as follows.

(1). When the sample intersects the triangular fuzzy function of the monotonous proposition, the ordinate of the intersection point is the support of the sample for the GBPA of the single subset proposition.

(2). When the sample intersects the fuzzy function of the triangle of the multi-subset proposition, the higher point of the ordinate of the intersection is the support of the sample point to the GBPA of the single subset proposition and the low point of the ordinate is the support of the sample for the GBPA of multiple subset propositions.

(3). When the sample intersects the triangular fuzzy number function of multiple multi-subset propositions, the ordinate height is the support of the sample for the GBPA of the single subset proposition and the ordinate low point is the support of the sample for the GBPA of the multi-subset proposition.

(4). If the sum of the support values of the GBPA generated above is greater than 1, normalize them. If the value is less than 1, the excess support value is assigned to the empty set.

The specific GBPA distribution formulas are shown in \( {Eq} \) . (12)-(13).

\[
S = \sum {w}_{i}
\]

\[
m\left( {A}_{1}\right)  = \frac{{w}_{1}}{S}
\]

\[
m\left( {A}_{2}\right)  = \frac{{w}_{2}}{S} \tag{12}
\]

\[
m\left( {{A}_{1},{A}_{2},{A}_{3}}\right)  = \frac{{w}_{3}}{S}
\]

\[
\text{ ... }
\]

\[
m\left( {{A}_{1},{A}_{2},{A}_{3},\ldots ,{A}_{m}}\right)  = \frac{{w}_{m}}{S}
\]

\[
m\left( \phi \right)  = \left\{  \begin{matrix} 0,\;\text{ if }\;S > 1 \\  1 - S,\;\text{ if }\;S \leq  1 \end{matrix}\right. \tag{13}
\]

When the GBPAs are combined, a vital problem is to decide whether the frame of discernment is complete or not. a threshold be determined in real applications.

Step 1.5: Calculate \( \overline{m\left( \phi \right) } \) , which is calculated as \( {Eq} \) . (14).

\[
\overline{m\left( \phi \right) } = \frac{1}{n}\mathop{\sum }\limits_{{i = 1}}^{n}{m}_{i}\left( \phi \right) \tag{14}
\]

Therefore, once \( \overline{m\left( \phi \right) } \) is calculated, the size of \( \overline{m\left( \phi \right) } \) and the threshold \( p \) can be used to determine whether the frame of discernment is complete or not. If \( \overline{m\left( \phi \right) } \) is greater than \( p \) , it is incomplete. otherwise, it is complete.

The criterion for determining whether the framework is complete is determined by the relative size of \( p \) and the degree of confidence assigned to the empty set has a physical meaning.

In GET, an empty set is treated as a focal element of the same property as other elements. The size of \( \overline{m\left( \phi \right) } \) represents the GBPA to support the incomplete frame of discernment. If the value of \( \overline{m\left( \phi \right) } \) is larger, the confidence that the GBPA support framework of discernment is incomplete will be greater. Assuming that \( p \) is a threshold, if the value of \( \overline{m\left( \phi \right) } \) exceeds this threshold, then the GBPA supports that the framework of discernment is incomplete.

## B. Step 2

When the frame of discernment is incomplete, it is necessary to re-update it. K-means clustering is an unsupervised clustering method that can cluster unlabeled data [54]. The main steps are as follows:

The K-means is mainly divided into four steps:

Step 2.1: For the central vector \( {C}_{1},{C}_{2}\ldots {C}_{K} \) initializes \( K \) seeds.

Step 2.2: Assign samples to the nearest center vector.

Step 2.3: The central vectors of each cluster are used as new centers.

Step 2.4: Repeat Step 2.2 and Step 2.3 until algorithm convergence.

Step 2.5: The Elbow method is viewed as one of the most useful methods to certain the optional numbers of category, because it is easy to interpret and verify through visualization. The Elbow method uses an error function as an indicator. As the number of clusters \( K \) increases, the sample partitioning will be more refined, and the degree of aggregation of each cluster will gradually increase, so the square of error cost function \( J \) will gradually become smaller. When \( K \) is smaller than the actual number of clusters, the increase in \( K \) will greatly increase the degree of aggregation of each cluster. So the decrease of cost function \( J \) will be large, and when \( K \) reaches the number of real clusters, the degree of polymerization obtained by adding \( K \) will be increased. The return will quickly become smaller, so the decline of cost function \( J \) will decrease sharply, and then tend to be flat as the value of \( \mathrm{k} \) continues to increase, that is, the relationship between cost function \( J \) and \( K \) is the shape of an elbow, and this elbow corresponds. The \( K \) value is the actual number of clusters of data. The formula of cost is shown in Eq. (8).

Finally, after the optimal \( K \) cluster is determined, it is necessary to update the frame of discernment. The following GBPAs are generated based on the updated frame of discernment.

## IV. EXPERIMENTS

## A. Experiments in Iris data sets

In this section, some experiments were performed to demonstrate the effectiveness of the method. Firstly, an incomplete frame of discernment is assumed. Based on this framework, the GBPA method is used to verify whether the frame of discernment is complete. Then, K-means clustering is used to cluster the train data, and the elbow method is used to determine the optimal cluster number. Finally update the frame of discernment and test the new frame of discernment through the test data set.

The Iris data [56] set has three categories in total: Iris setosa (a), Iris versicolor (b), Iris virginica (c). There are 50 samples in each category, with 4 attributes, sepal length (SL), sepal with (SW), petal length (PL), petal with (PW).

The entire data set is firstly divided into: train and test data set, each of which accounts for 60% and 40% of the total data set, respectively. 30 samples as the train data set are randomly selected from each category, and 20 are used as test data set of the each category.

For the Iris data-set, four different frame of discernment are shown as follows.

\[
{\Omega }_{1} = \{ a, b\} \;{\Omega }_{2} = \{ a, c\} \;{\Omega }_{3} = \{ b, c\} \;{\Omega }_{4} = \{ a, b, c\}
\]

For example, for the frame of discernment \( {\Omega }_{2} \) , the system knows target \( a \) and target \( c \) , but doesn’t know target \( b \) . The frame of discernment at this time is incomplete. Therefore, it is necessary to judge whether the frame of discernment is complete or not.

The first step is to identify whether the frame of discernment is complete or not. Create a triangular fuzzy model based on train data set, as shown in Eq. (15).

\[
f\left( {x}_{i}^{j}\right)  = \left\{  \begin{matrix} 0 & {x}_{i}^{j} < \mathop{\min }\limits_{{1 \leq  i \leq  n}}\left( {x}_{i}^{j}\right) \\  \frac{{x}_{i}^{j} - \mathop{\min }\limits_{{1 \leq  i \leq  n}}\left( {x}_{i}^{j}\right) }{\frac{1}{n}\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}^{j} - \mathop{\min }\limits_{{1 \leq  i \leq  n}}\left( {x}_{i}^{j}\right) } & \mathop{\min }\limits_{{1 \leq  i \leq  n}}\left( {x}_{i}^{j}\right)  \leq  {x}_{i}^{j} \leq  \frac{1}{n}\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}^{j} \\  \frac{-{x}_{i}^{j} + \mathop{\max }\limits_{{1 \leq  i \leq  n}}\left( {x}_{i}^{j}\right) }{\frac{1}{n}\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}^{j} + \mathop{\max }\limits_{{1 \leq  i \leq  n}}\left( {x}_{i}^{j}\right) } & \frac{1}{n}\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}^{j} < {x}_{i}^{j} \leq  \mathop{\max }\limits_{{1 \leq  i \leq  n}}\left( {x}_{i}^{j}\right) \\  0 & {x}_{i}^{j} > \mathop{\max }\limits_{{1 \leq  i \leq  n}}\left( {x}_{i}^{j}\right)  \end{matrix}\right. \tag{15}
\]

where \( i = 1,\ldots ,{30}, j = 1,2,3,4 \) . In the Iris data set respectively indicate that there are 30 samples in each train data set, and each category has 4 attributes.

The specific triangular fuzzy model information for each category is shown in TABLE I .

TABLE I: Specific construction information in Iris

<table><tr><td>Standard</td><td></td><td></td></tr><tr><td>category</td><td>\{a\} SL, SW, PL, PW</td><td>\{c\} SL, SW, PL, PW</td></tr><tr><td>Number of samples</td><td>30</td><td>30</td></tr><tr><td>Attribute minimum</td><td>4.4, 2.3, 1, 0.1</td><td>5.7, 2.2, 4.8, 1.4</td></tr><tr><td>Attribute average</td><td>5.0, 3.4, 1.4, 0.2</td><td>6.5, 2.9, 5.4, 2.0</td></tr><tr><td>Attribute maximum</td><td>5.8, 4.4, 1.7, 0.6</td><td>7.7, 3.8, 6.7, 2.5</td></tr></table>

Fig. (2)-(5) shows the GBPA obtained based on four attributes. The subgraph \( \left( a\right)  - \left( d\right) \) are the GBPA generated according to the attribute \( {SL},{SW},{PL},{PW} \) .

![bo_d4hrgfjef24c739bj2p0_4_517_222_738_502_0.jpg](images/bo_d4hrgfjef24c739bj2p0_4_517_222_738_502_0.jpg)

Fig. 2: Triangular Fuzzy method generates GBPA

![bo_d4hrgfjef24c739bj2p0_4_518_896_737_502_0.jpg](images/bo_d4hrgfjef24c739bj2p0_4_518_896_737_502_0.jpg)

Fig. 3: Triangular Fuzzy method generates GBPA

![bo_d4hrgfjef24c739bj2p0_4_518_1572_739_502_0.jpg](images/bo_d4hrgfjef24c739bj2p0_4_518_1572_739_502_0.jpg)

Fig. 4: Triangular Fuzzy method generates GBPA

![bo_d4hrgfjef24c739bj2p0_5_518_181_734_500_0.jpg](images/bo_d4hrgfjef24c739bj2p0_5_518_181_734_500_0.jpg)

Fig. 5: Triangular Fuzzy method generates GBPA

Then use the Eq. (12)-(13) to allocate GBPA method, calculate the value of \( \mathrm{m} \) , the specific value is shown in TABLE II .

TABLE II: Average value on each attribute of GBPA

<table><tr><td>SL</td><td>SW</td><td>PL</td><td>PW</td><td>mean</td></tr><tr><td>0.5016</td><td>0.3815</td><td>0.7775</td><td>0.6858</td><td>0.5866</td></tr></table>

According to the discussion [38] and reasonable experiment results, the threshold \( p \) is set to 0.5 .

Therefore, the frame of discernment at this time is judged to be incomplete. It is necessary to re-determine the number of clusters according to K-means clustering. At this time, the number of target in frame of discernment is 2 , and when the number of unknowns exceeds 2, that is, when the number of unknown targets exceeds the number of knows, the system is considered to be inoperable.

Then determine the correct number of clusters according to the Elbow method . Its calculation formula is shown in Eq. (8). The specific drop curve of cost function \( J \) is shown in Fig. 6.

![bo_d4hrgfjef24c739bj2p0_5_217_1388_619_438_0.jpg](images/bo_d4hrgfjef24c739bj2p0_5_217_1388_619_438_0.jpg)

Fig. 6: The descent curve of cost function \( J \)

It can be seen that when the curve has an inflection point at \( K = 3 \) , the judgment category should be three categories, which is consistent with the actual number of categories.

After determining the number of new frame of discernment, the frame of discernment needs to be updated. Repeating the process of Step one, in which a new GBPA is generated as shown in Fig. (7)-(10).

Calculate value of the \( m\left( \phi \right) \) again using Eq. (12)-(13). The results are shown in TABLE III.

TABLE III: The new model's average GBPA value on each attribute

<table><tr><td>SL</td><td>SW</td><td>PL</td><td>PW</td><td>mean</td></tr><tr><td>0.2793</td><td>0.3114</td><td>0.6177</td><td>0.5031</td><td>0.4279</td></tr></table>

Where the value of the \( m\left( \phi \right) \) set is smaller than the threshold of 0.5 , then the frame of discernment is considered complete.

The test data is used to verify the rationality of the updated frame of discernment. First, use the new frame of discernment to generate GBPA for each test data. The new GBPA can be calculated through Eq. (12)-(13). In order to make final decision, it is necessary to convert each GBPA into a probability using Eq. (7). Finally, the decision process is to combine the probabilities generated by the attributes of each sample, and then take the most probable target as the judgment.

The test results of the final test set are shown in TABLE IV.

Where the category \( a \) and category \( c \) achieve very high accuracy, and the increased category \( b \) achieves 90% accuracy.

## B. Further Experiments

In order to further verify the validity of the proposed method, the optimal cluster number was determined in the data set glass, haberman, Knowledge, seeds, WDBC, Aggregation, Cancer and Robotnavigation from UCI data sets website [57], [58], [59], [60], [61]. where the details of dataset can be seen in TABLE V.

we compare the proposed method with other related methods [62], [63]. The proposed method is divided into two steps: the first step is to identify whether the framework is complete. The second step is to identify the number of targets. Therefore, the experiments are also divided into two types, the first one is compared with the algorithm that identifies the complete frame of discernment, and the second is compared with the unsupervised clustering indicators [64], [65].

First, Jiang [62] and Sun [63] recently proposed new methods to identify whether the framework is complete or not. The proposed method is compared with them. Suppose the system system can only identify two targets, the results are shown in Fig. 11, 12 and TABLE VI.

Results show that all methods accurately identify whether the frame of discernment is complete or not, further the proposed method identifies the number of unknown targets.

Second, because the Euclidean distance is the measured distance in the K-means algorithm, two indicators of unsupervised clustering based on Euclidean distance are compared with the proposed method. They are Calinski-Harabasz Criterion [64] and Davies-Bouldin Criterion [65].

![bo_d4hrgfjef24c739bj2p0_6_518_186_737_500_0.jpg](images/bo_d4hrgfjef24c739bj2p0_6_518_186_737_500_0.jpg)

Fig. 7: Triangular Fuzzy method generates GBPA

![bo_d4hrgfjef24c739bj2p0_6_517_786_737_501_0.jpg](images/bo_d4hrgfjef24c739bj2p0_6_517_786_737_501_0.jpg)

Fig. 8: Triangular Fuzzy method generates GBPA

![bo_d4hrgfjef24c739bj2p0_6_517_1387_740_499_0.jpg](images/bo_d4hrgfjef24c739bj2p0_6_517_1387_740_499_0.jpg)

Fig. 9: Triangular Fuzzy method generates GBPA

TABLE IV: The classification results

<table><tr><td>category</td><td>category size</td><td>Proper Amount</td><td>Accuracy rate</td></tr><tr><td>\{a\}</td><td>10</td><td>10</td><td>100%</td></tr><tr><td>\{b\}</td><td>10</td><td>9</td><td>90%</td></tr><tr><td>\{c\}</td><td>10</td><td>10</td><td>100%</td></tr><tr><td>TOTAL</td><td>30</td><td>29</td><td>93%</td></tr></table>

![bo_d4hrgfjef24c739bj2p0_7_518_213_737_501_0.jpg](images/bo_d4hrgfjef24c739bj2p0_7_518_213_737_501_0.jpg)

Fig. 10: Triangular Fuzzy method generates GBPA

TABLE V: Information in eight data sets

<table><tr><td>Data sets</td><td>Number of instances</td><td>Number of attributes</td><td>Numbers of types</td></tr><tr><td>glass</td><td>214</td><td>20</td><td>6</td></tr><tr><td>haberman</td><td>306</td><td>3</td><td>2</td></tr><tr><td>Knowledge Modeling</td><td>403</td><td>5</td><td>4</td></tr><tr><td>seeds</td><td>210</td><td>7</td><td>3</td></tr><tr><td>WDBC</td><td>569</td><td>30</td><td>2</td></tr><tr><td>Aggregation</td><td>788</td><td>2</td><td>7</td></tr><tr><td>Cancer</td><td>683</td><td>9</td><td>2</td></tr><tr><td>Robotnavigation</td><td>5456</td><td>24</td><td>5</td></tr></table>

![bo_d4hrgfjef24c739bj2p0_7_253_1260_1339_802_0.jpg](images/bo_d4hrgfjef24c739bj2p0_7_253_1260_1339_802_0.jpg)

Fig. 11: Curves of the Elbow method on four data sets

![bo_d4hrgfjef24c739bj2p0_8_235_179_1323_823_0.jpg](images/bo_d4hrgfjef24c739bj2p0_8_235_179_1323_823_0.jpg)

Fig. 12: Curves of the Elbow method on four other data sets

TABLE VI: Futher experments of eight data sets

<table><tr><td>Data sets</td><td>Real number of category</td><td>Proposed's method detects number of category</td><td>Complete Frame of discernment (Yes or No) proposed method</td><td>Jiang's method [62]</td><td>Sun's method [63]</td></tr><tr><td>glass</td><td>6</td><td>3</td><td>No</td><td>No</td><td>No</td></tr><tr><td>haberman</td><td>2</td><td>2</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Knowledge Modeling</td><td>4</td><td>4</td><td>No</td><td>No</td><td>No</td></tr><tr><td>seeds</td><td>3</td><td>3</td><td>No</td><td>No</td><td>No</td></tr><tr><td>WDBC</td><td>2</td><td>2</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Aggregation</td><td>7</td><td>5</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Cancer</td><td>2</td><td>2</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Robotnavigation</td><td>5</td><td>5</td><td>No</td><td>No</td><td>No</td></tr></table>

The Calinski-Harabasz index is defined as folllows [64].

\[
{CH} = \frac{\mathop{\sum }\limits_{{i = 1}}^{k}{n}_{i}{\left| {m}_{i} - m\right| }^{2}}{\mathop{\sum }\limits_{{i = 1}}^{k}\mathop{\sum }\limits_{{x \in  {C}_{i}}}{\left| x - {m}_{i}\right| }^{2}} \times  \frac{N - k}{k - 1}
\]

Where \( k \) is the number of clusters, \( {m}_{k} \) is the centroid of cluster \( k, m \) is the overall mean of datasets, and \( {\left| {m}_{k} - m\right| }^{2} \) is the Euclidean distance between the two vectors.

The optimal clustering number has the highest CH value [64].

The Davies-Bouldin index is defined as follows [65].

\[
{DB} = \frac{1}{k}\mathop{\sum }\limits_{{i = 1}}^{k}\mathop{\max }\limits_{{j \neq  i}}{D}_{i, j}\;{D}_{i, j} = \frac{{\bar{d}}_{i} + {\bar{d}}_{j}}{{d}_{i, j}}
\]

Where \( {\bar{d}}_{k} \) is the average distance between each point in the \( {kth} \) cluster and the centroid of the \( {kth} \) cluster and \( {d}_{i, j} \) is the Euclidean distance between the centroids of the ith and jth clusters. The maximum value of \( {D}_{i, j} \) represents the erost case and the optimal clustering number has the smallest DB value [65].

Because, the indicator CH [64] and DB [65] require \( k > 1 \) , \( k \) starts from 2 to 10. As can be seen from the in TABLE VII, not all unsupervised clustering indicators can accurately determine the number of targets each time. The Elbow method accurately judges the number of unknown targets on 6 data sets. The three methods differed significantly in the data set glass and Aggregation. Although K-means algorithm is a classic algorithm for solving clustering problems, it also has some shortcomings. First, K-means belongs to the distance-based clustering algorithm and uses distance as the similarity index. The closer the distance between the two targets, the greater their similarity. However, when the two target clusters are close, especially when the data of one target is small, K-means can easily determine the two clusters as a type of target. Second, K-means is sensitive to noise and isolated point data. The K-means algorithm treats the cluster's centred as the center of the cluster and adds it to the next round of calculations, so a small amount of this type of data has a great impact on the average, resulting in unstable or even wrong results. This is why the three methods have a large difference in data-set glass and data-set Aggregation. For the sample-balanced data set of Cancer, all three methods consistently consider the number of targets to be 2.

TABLE VII: Further experiments in other eight data sets

<table><tr><td></td><td>k=2</td><td>k=3</td><td>k=4</td><td>k=5</td><td>k=6</td><td>k=7</td><td>k=8</td><td>k=9</td><td>k=10</td><td>optimal k</td></tr><tr><td colspan="11">glass</td></tr><tr><td>CH</td><td>134.5973</td><td>96.7330</td><td>121.2692</td><td>83.4533</td><td>87.2031</td><td>54.6102</td><td>115.5704</td><td>96.9375</td><td>97.9003</td><td>2</td></tr><tr><td>DB</td><td>1.0190</td><td>1.0189</td><td>0.8968</td><td>1.1364</td><td>1.0114</td><td>1.2219</td><td>0.7647</td><td>1.0175</td><td>0.9405</td><td>8</td></tr><tr><td>proposed method</td><td>0.0266</td><td>0.0157</td><td>0.0116</td><td>0.0072</td><td>0.0065</td><td>0.0053</td><td>0.0038</td><td>0.0036</td><td>0.0030</td><td>3</td></tr><tr><td colspan="11">harberman</td></tr><tr><td>CH</td><td>239.4597</td><td>239.1752</td><td>183.7976</td><td>225.8340</td><td>218.6951</td><td>190.8015</td><td>215.3999</td><td>205.8548</td><td>187.0251</td><td>2</td></tr><tr><td>DB</td><td>0.9604</td><td>0.8474</td><td>0.8603</td><td>0.8699</td><td>1.0661</td><td>1.0699</td><td>1.1337</td><td>1.0425</td><td>1.0603</td><td>3</td></tr><tr><td>proposed method</td><td>1.6662</td><td>1.2404</td><td>0.9911</td><td>0.8128</td><td>0.7306</td><td>0.6772</td><td>0.6278</td><td>0.5736</td><td>0.5521</td><td>2</td></tr><tr><td colspan="11">knowledge</td></tr><tr><td>CH</td><td>236.4534</td><td>271.4546</td><td>378.7307</td><td>311.0565</td><td>268.1914</td><td>246.9609</td><td>246.9040</td><td>182.9647</td><td>206.2843</td><td>4</td></tr><tr><td>DB</td><td>0.7384</td><td>0.7302</td><td>0.8665</td><td>1.0407</td><td>1.4774</td><td>1.1874</td><td>1.5019</td><td>1.4022</td><td>1.5436</td><td>3</td></tr><tr><td>proposed method</td><td>0.0036</td><td>0.0024</td><td>0.0018</td><td>0.0018</td><td>0.0015</td><td>0.0014</td><td>0.0013</td><td>0.0013</td><td>0.0011</td><td>4</td></tr><tr><td colspan="11">seeds</td></tr><tr><td>CH</td><td>351.1800</td><td>375.8050</td><td>288.3381</td><td>310.3318</td><td>256.6166</td><td>269.0777</td><td>263.8357</td><td>281.2261</td><td>261.6489</td><td>3</td></tr><tr><td>DB</td><td>0.6664</td><td>0.7533</td><td>0.9787</td><td>0.9153</td><td>0.9884</td><td>0.9467</td><td>0.9237</td><td>1.0008</td><td>0.9280</td><td>2</td></tr><tr><td>proposed method</td><td>0.0062</td><td>0.0019</td><td>0.0039</td><td>0.0040</td><td>0.0040</td><td>0.0041</td><td>0.0035</td><td>0.0033</td><td>0.0027</td><td>3</td></tr><tr><td colspan="11">WDBC</td></tr><tr><td>CH</td><td>1300.2082</td><td>1246.2607</td><td>1444.5180</td><td>1621.0110</td><td>1466.0654</td><td>1588.8407</td><td>1632.5261</td><td>1590.7458</td><td>1624.5511</td><td>8</td></tr><tr><td>DB</td><td>0.5044</td><td>0.6329</td><td>0.6057</td><td>0.6447</td><td>0.6486</td><td>0.6557</td><td>0.7526</td><td>0.6722</td><td>0.7776</td><td>2</td></tr><tr><td>proposed method</td><td>0.0210</td><td>0.0599</td><td>0.1396</td><td>0.1231</td><td>0.0543</td><td>0.0203</td><td>0.1462</td><td>0.0317</td><td>0.0834</td><td>2</td></tr><tr><td colspan="11">Aggregation</td></tr><tr><td>CH</td><td>686.7868</td><td>1035.4891</td><td>1136.0906</td><td>1082.5220</td><td>1160.5725</td><td>1404.6364</td><td>1342.8805</td><td>1235.8415</td><td>1288.1291</td><td>7</td></tr><tr><td>DB</td><td>0.9101</td><td>0.6710</td><td>0.7693</td><td>0.7064</td><td>0.6412</td><td>0.7220</td><td>0.8299</td><td>0.7394</td><td>0.7955</td><td>6</td></tr><tr><td>proposed method</td><td>0.1565</td><td>0.0799</td><td>0.0474</td><td>0.0193</td><td>0.0435</td><td>0.0188</td><td>0.0101</td><td>0.0113</td><td>0.0036</td><td>5</td></tr><tr><td colspan="11">Cancer</td></tr><tr><td>CH</td><td>1.0263e+03</td><td>673.1458</td><td>491.2794</td><td>429.5671</td><td>365.7954</td><td>324.7845</td><td>306.0923</td><td>285.0813</td><td>260.6512</td><td>2</td></tr><tr><td>DB</td><td>0.7573</td><td>1.5347</td><td>1.6797</td><td>1.6571</td><td>1.7048</td><td>1.7010</td><td>1.6151</td><td>1.5920</td><td>1.6601</td><td>2</td></tr><tr><td>proposed method</td><td>0.0677</td><td>0.0708</td><td>0.0762</td><td>0.0739</td><td>0.0613</td><td>0.0717</td><td>0.0701</td><td>0.0788</td><td>0.0721</td><td>2</td></tr><tr><td colspan="11">Robotnavigation</td></tr><tr><td>CH</td><td>7209.8465</td><td>8715.5389</td><td>8642.1590</td><td>13006.4244</td><td>17252.5960</td><td>16151.8541</td><td>16182.5750</td><td>15824.5242</td><td>16397.0430</td><td>6</td></tr><tr><td>DB</td><td>0.7944</td><td>0.6787</td><td>0.6866</td><td>0.4802</td><td>0.5231</td><td>0.6326</td><td>0.6695</td><td>0.6528</td><td>0.6469</td><td>5</td></tr><tr><td>proposed method</td><td>0.0108</td><td>0.0098</td><td>0.0078</td><td>0.0072</td><td>0.0071</td><td>0.0069</td><td>0.0071</td><td>0.0068</td><td>0.0068</td><td>5</td></tr></table>

## V. Conclusion

In this paper, a cluster-based approach is proposed to detect the number of unknown targets in the open world.

First step is to judge whether the frame of discernment is in open world. if the frame of discernment is incomplete, using K-means clustering to cluster targets. Finally, Elbow method is used to find an optimal number of elements and re-update the frame of discernment. To the best of our knowledge, this is the first attempt to use a cluster-based approach to solve the problem of determining the number of targets in the open world.

Experiments show the efficiency of our proposed method to solve the proposed method. However, it seems that, in some cases, the Elbow method does not accurately identify the number of targets. In the future, how to deal with the sample imbalance data, so that the number of targets can be more accurately identified is still a problem that needs to be improved.

## ACKNOWLEDGMENT

The authors greatly appreciate the reviews' suggestions and the editor's encouragement.

## REFERENCES

[1] Arthur P Dempster. Upper and lower probabilities induced by a multivalued mapping. The annals of mathematical statistics, pages 325-339, 1967.

[2] Glenn Shafer et al. A mathematical theory of evidence, volume 1. Princeton university press Princeton, 1976.

[3] Palash Dutta. An uncertainty measure and fusion rule for conflict evidences of big data via dempstershafer theory. International Journal of Image and Data Fusion, 9(2):152-169, 2018.

[4] Palash Dutta. Modeling of variability and uncertainty in human health risk assessment. MethodsX, 4:76 - 85, 2017.

[5] Hamidreza Seiti and Ashkan Hafezalkotob. Developing pessimisti-coptimistic risk-based methods for multi-sensor fusion: An interval-valued evidence theory approach. Applied Soft Computing, 72:609 - 623, 2018.

[6] Ronald R. Yager. Entailment for measure based belief structures. Information Fusion, 47:111 - 116, 2019.

[7] Ronald R. Yager, Paul Elmore, and Fred Petry. Soft likelihood functions in combining evidence. Information Fusion, 36:185-190, 2017.

[8] Z. Liu, Q. Pan, J. Dezert, J. Han, and Y. He. Classifier fusion with contextual reliability evaluation. IEEE Transactions on Cybernetics, 48(5):1605-1618, May 2018.

[9] Zhun ga Liu, Yong Liu, Jean Dezert, and Quan Pan. Classification of incomplete data based on belief functions and k-nearest neighbors. Knowledge-Based Systems, 89:113 - 125, 2015.

[10] Yangxue Li and Yong Deng. TDBF: Two Dimension Belief Function. International Journal of Intelligent Systems, 34(8):1968-1982, 2019.

[11] Xiaozhuan Gao, Fan Liu, Lipeng Pan, Yong Deng, and Sang-Bing Tsai. Uncertainty measure based on Tsallis entropy in evidence theory. International Journal of Intelligent Systems, 34(11):3105-3120, 2019.

[12] Fuyuan Xiao. Multi-sensor data fusion based on the belief divergence measure of evidences and the belief entropy. Information Fusion, 46(2019):23-32, 2019.

[13] Liguo Fei and Yong Deng. A new divergence measure for basic probability assignment and its applications in extremely uncertain environments. International Journal of Intelligent Systems, 34(4):584- 600, 2019.

[14] Xiaoge Zhang, Sankaran Mahadevan, and Xinyang Deng. Reliability analysis with linguistic data: An evidential network approach. Reliability Engineering & System Safety, 162:111-121, 2017.

[15] Hongming Mo and Yong Deng. Identifying node importance based on evidence theory in complex networks. Physica A: Statistical Mechanics & Its Applications, page 10.1016/j.physa.2019.121538, 2019.

[16] Fuyuan Xiao. EFMCDM: Evidential fuzzy multicriteria decision making based on belief entropy. IEEE Transactions on Fuzzy Systems, page DOI: 10.1109/TFUZZ.2019.2936368, 2019.

[17] Yu-Ting Liu, Nikhil R Pal, Amar R Marathe, Yu-Kai Wang, and Chin-Teng Lin. Fuzzy decision-making fuser (fdmf) for integrating human-machine autonomous (hma) systems with adaptive evidence sources. Frontiers in neuroscience, 11:332, 2017.

[18] Hamidreza Seiti and Ashkan Hafezalkotob. Developing the r-topsis methodology for risk-based preventive maintenance planning: A case study in rolling mill company. Computers & Industrial Engineering, 128:622-636, 2019.

[19] Yuanna Liu and Wen Jiang. A new distance measure of interval-valued intuitionistic fuzzy sets and its application in decision making. Soft Computing, 23:10.1007/s00500-019-04332-5, 2019.

[20] Hongming Mo and Yong Deng. An evaluation for sustainable mobility extended by D numbers. Technological and Economic Development of Economy, 25(5):802-819, 2019.

[21] Hamidreza Seiti, Ashkan Hafezalkotob, and Reza Fattahi. Extending a pessimisticoptimistic fuzzy information axiom based approach considering acceptable risk: Application in the selection of maintenance strategy. Applied Soft Computing, 67:895 - 909, 2018.

[22] Thierry Denoeux. A k-nearest neighbor classification rule based on dempster-shafer theory. IEEE transactions on systems, man, and cybernetics, 25(5):804-813, 1995.

[23] Mustafa Mezaal, Biswajeet Pradhan, and Hossein Rizeei. Improving landslide detection from airborne laser scanning data using optimized dempstershafer. Remote Sensing, 10:1029, 06 2018.

[24] Behnaz Bigdeli and Parham Pahlavani. High resolution multisensor fusion of sar, optical and lidar data based on crisp vs. fuzzy and feature vs. decision ensemble systems. International journal of applied earth observation and geoinformation, 52:126-136, 2016.

[25] Thierry Denoeux. A neural network classifier based on dempster-shafer theory. IEEE Transactions on Systems, Man, and Cybernetics-Part A: Systems and Humans, 30(2):131-150, 2000.

[26] Xinyang Deng and Wen Jiang. An evidential axiomatic design approach for decision making using the evaluation of belief structure satisfaction to uncertain target values. International Journal of Intelligent Systems, 33(1):15-32.

[27] Yafei Song, Xiaodan Wang, Lei Lei, and Shaohua Yue. Uncertainty measure for interval-valued belief structures. Measurement, 80:241- 250, FEB 2016.

[28] Wen Jiang, Boya Wei, Xiang Liu, Xiaoyang Li, and Hanqing Zheng. Intuitionistic fuzzy power aggregation operator based on entropy and its application in decision making. International Journal of Intelligent Systems, 33(1):49-67.

[29] Fuyuan Xiao. A novel multi-criteria decision making method for assessing health-care waste treatment technologies based on D numbers. Engineering Applications of Artificial Intelligence, 71(2018):216-225, 2018.

[30] Xihua Li and Xiaohong Chen. D-Intuitionistic Hesitant Fuzzy Sets and their Application in Multiple Attribute Decision Making. COGNITIVE COMPUTATION, 10(3):496-505, JUN 2018.

[31] Weiquan Zhang and Yong Deng. Combining conflicting evidence using the DEMATEL method. Soft computing, 23:8207-8216, 2019.

[32] Jian-Bo Yang and Dong-Ling Xu. Evidential reasoning rule for evidence combination. Artificial Intelligence, 205:1 - 29, 2013.

[33] Johan Schubert. Conflict management in dempstershafer theory using the degree of falsity. International Journal of Approximate Reasoning, 52:449-460, 2011.

[34] Catherine K. Murphy. Combining belief functions when evidence conflicts. Decision Support Systems, 29:1-9, 2000.

[35] Yujuan Wang, Kezhen Zhang, and Yong Deng. Base belief function: an efficient method of conflict management. Journal of Ambient Intelligence and Humanized Computing, 10(9):3427-3437, 2019.

[36] Honghui Xu and Yong Deng. Dependent evidence combination based on decision-making trial and evaluation laboratory method. International Journal of Intelligent Systems, 34(7):1555-1571, 2019.

[37] Yong Deng. Generalized evidence theory. Applied Intelligence, 43(3):530-543, Oct 2015.

[38] Wen Jiang, Yue Chang, and Shiyu Wang. A method to identify the incomplete framework of discernment in evidence theory. Mathematical Problems in Engineering, 2017, 2017.

[39] Stuart Lloyd. Least squares quantization in pcm. IEEE transactions on information theory, 28(2):129-137, 1982.

[40] Robert L Thorndike. Who belongs in the family? Psychometrika, 18(4):267-276, 1953.

[41] Ronald R. Yager. Uncertainty modeling using fuzzy measures. Knowledge-Based Systems, 92:1-8, 2016.

[42] Zhunga Liu, Quan Pan, Jean Dezert, and Arnaud Martin. Combination of classifiers with optimal weight based on evidential reasoning. IEEE Transactions on Fuzzy Systems, PP(99):1-15, 2017.

[43] Y. Liu, N. R. Pal, A. R. Marathe, and C. Lin. Weighted fuzzy dempstershafer framework for multimodal information integration. IEEE Transactions on Fuzzy Systems, 26(1):338-352, Feb 2018.

[44] Huchang Liao, Zeshui Xu, and Xiao-Jun Zeng. Distance and similarity measures for hesitant fuzzy linguistic term sets and their application in multi-criteria decision making. Information Sciences, 271:125 - 142, 2014.

[45] Huchang Liao, Ming Tang, Zongmin Li, and Benjamin Lev. Bib-liometric analysis for highly cited papers in operations research and management science from 2008 to 2017 based on essential science indicators. Omega, DOI:10.1016/j.omega.2018.11.005 2018.

[46] Yongchuan Tang, Deyun Zhou, and Felix Chan. An extension to dengs entropy in the open world assumption with an application in sensor data fusion. Sensors, 18(6):1902, 2018.

[47] Wen Jiang, Shiyu Wang, Xiang Liu, Hanqing Zheng, and Boya Wei. Evidence conflict measure based on owa operator in open world. PLOS ONE, 12(5):1-18, 05 2017.

[48] Wen Jiang and Jun Zhan. A modified combination rule in generalized evidence theory. Applied Intelligence, 46, 10 2016.

[49] Milan Daniel. A relationship of conflicting belief masses to open world assumption. In International Conference on Belief Functions, pages 146-155. Springer, 2016.

[50] Wen Jiang. A correlation coefficient for belief functions. International Journal of Approximate Reasoning, 103:94-106, 2018.

[51] Xiaoyan Su, Lusu Li, Fengjian Shi, and Hong Qian. Research on the fusion of dependent evidence based on mutual information. IEEE Access, 6:71839-71845, 2018.

[52] Xiaoyan Su, Lusu Li, Hong Qian, Mahadevan Sankaran, and Yong Deng. A new rule to combine dependent bodies of evidence. Soft Computing, 23(20):9793-9799, 2019.

[53] Philippe Smets and Robert Kennes. The transferable belief model. Artificial Intelligence, 66(2):191 - 234, 1994.

[54] James MacQueen et al. Some methods for classification and analysis of multivariate observations. In Proceedings of the fifth Berkeley symposium on mathematical statistics and probability, volume 1, pages 281-297. Oakland, CA, USA, 1967.

[55] Renliang Sun and Yong Deng. A new method to determine generalized basic probability assignment in the open world. IEEE Access, 7(1):52827-52835, 2019.

[56] Ronald A Fisher. The use of multiple measurements in taxonomic problems. Annals of eugenics, 7(2):179-188, 1936.

[57] Zhong Ping and Masao Fukushima. Regularized nonsmooth newton method for multi-class support vector machines. Optimization Methods Software, 22(1):225-236, 2007.

[58] Kai Ming Ting and Ian H Witten. Issues in stacked generalization. Journal of Artificial Intelligence Research, 10(1):271-289, 2002.

[59] H. Tolga Kahraman, Seref Sagiroglu, and Ilhami Colak. The development of intuitive knowledge classifier and the modeling of domain dependent data. Know.-Based Syst., 37:283-295, January 2013.

[60] Giorgio Valentini and Francesco Masulli. Neurobjects : an object-oriented library for neural network development. Neurocomputing, 48(1):623-646, 2002.

[61] Dua Dheeru and Efi Karra Taniskidou. UCI machine learning repository, http://archive.ics.uci.edu/ml, 2017.

[62] Wen Jiang, Jun Zhan, Deyun Zhou, and Xin Li. A method to determine generalized basic probability assignment in the open world. Mathematical Problems in Engineering,2016,(2016-5-24), 2016(2):1- 11, 2016.

[63] Renliang Sun and Yong Deng. A new method to identify incomplete frame of discernment in evidence theory. IEEE Access, 7:15547- 15555, 2019.

[64] Tadeusz Caliński and Jerzy Harabasz. A dendrite method for cluster analysis. Communications in Statistics-theory and Methods, 3(1):1- 27, 1974.

[65] David L Davies and Donald W Bouldin. A cluster separation measure. IEEE transactions on pattern analysis and machine intelligence, (2):224-227, 1979.

IEEE TRANSACTION ON FUZZY SYSTEMS, VOL., NO., OCTOBER 2018

![bo_d4hrgfjef24c739bj2p0_11_161_181_225_275_0.jpg](images/bo_d4hrgfjef24c739bj2p0_11_161_181_225_275_0.jpg)

Fan Liu is a Junior student at the Yingcai Honors college of Mathematics and Physics Basic Science (Academic Talent Program) at the University of Electronic Science and Technology of China. In December 2017, Fan was appointed as research assistant in Institute of Fundamental and Frontier Science at the University of Electronic Science and Technology of China. Fan worked with Prof. Deng here in Evidence theory. Fan's research direction is in evidence theory, and he is interested in machine learning, quantum computing, and uncertainty analysis. Fan received a national scholarship and outstanding student scholarship in 2018.

![bo_d4hrgfjef24c739bj2p0_11_168_1041_208_277_0.jpg](images/bo_d4hrgfjef24c739bj2p0_11_168_1041_208_277_0.jpg)

Yong Deng received the Ph.D. degree in Precise Instrumentation from Shanghai Jiao Tong University, Shanghai, China, in 2003. From 2005 to 2011, he was an Associate Professor in the Department of Instrument Science and Technology, Shanghai Jiao Tong University. From 2010, he was a Professor in the School of Computer and Information Science, Southwest University, Chongqing, China. From 2012, he was a Visiting Professor in Vanderbilt University, Nashville, TN, USA. From 2016, he was also a Professor in School of Electronic and Information Engineering, Xi'an Jiaotong University, Xian, China. From 2017, he is the full professor of Institute of Fundamental and Frontier Science, University of Electronic Science and Technology of China, Chengdu, China. From 2017, he is the adjct professor of Medical center, Vanderbilt University, Nashville, TN, USA. Professor Deng has published more than 100 papers in referred journals. His research interests include evidence theory, decision making, information fusion and complex system modelling. He severed as the program member of many conference such as International Conference on Belief Functions. He severed as many editorial board members such as Editorial Board Member of Applied Intelligence and Journal of Organizational and End User Computing. He severed as many guest editor such as International Journal of Approximate Reasoning, Mathematical Problems in Engineering and Sustainability. He severed as the reviewer for more than 30 journals. Professor Deng has received numerous honors and awards, including the Elsevier Highly Cited Scientist in China from 2014 to present.
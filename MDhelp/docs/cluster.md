<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="Cluster_Analysis"></a>
# Cluster Analysis data tree entry

The Cluster Analysis data tree entry shows parameters to perform a cluster analysis computation and results from that analysis once it has been run. This data tree entry is created in GSAS-II after the main menu command **Calculate/Setup Cluster Analysis** is used. 

Cluster analysis is a suite of data survey techniques where data are grouped by some measure of their similarity. Thus, it can be used as a preliminary survey of a large number of data sets in e.g. preparation of detailed examination of representative members. In the case of powder diffraction pattern (PWDR) data or pair distribution (PDF) data, their similarity is determined by considering each pattern as a hyper-dimensional vector with one dimension for each data point and then computing some measure of how parallel pairs of these vectors are. Consequently, it can be used to survey PWDR data entries that have identical scan characteristics (e.g. instrument type, step size, radiation type, wavelength) or multiple PDF G(r) entries created with the same step sizes and using the same radiation from data collected with identical instrument configurations. The cluster analysis routines used here are from the scipy library and (if available) the scikit-learn library.  If scikit-learn is absent, an attempt is automatically made to install the latter via the conda system. The scipy library provides some cluster analysis tools while the scikit-learn package provides others. If you use results from scikit-learn, please cite the following in any publication that uses it:

: "Scikit-learn: Machine Learning in Python", Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M. and Duchesnay, E., (2011). Journal of Machine Learning Research 12, 2825-2830.

## Cluster Analysis with scipy

Doing cluster analysis in GSAS-II requires several steps; new steps will become visible in the GUI as previous ones are completed. Redoing earlier steps may clear subsequent ones. For an example, see the tutorial, [Cluster and Outlier Analysis](https://advancedphotonsource.github.io/GSAS-II-tutorials/ClusterAnalysis/Cluster%20and%20Outlier%20Analysis.htm).

In order of their appearance, the GUI commands are:

* **Select datasets** - this brings up a selection tool for PWDR (& PDF, if present) entries in the GSAS-II data tree. Your selection must be either PWDR or PDF data; otherwise, there is no check on data similarity so be careful with your selections. Multi-bank TOF data should not be mixed for cluster analysis nor should laboratory and synchrotron data. Cluster analysis on fewer than 5-10 data sets is probably not useful, but can be applied on dozens or even hundreds of data sets.
* **Data limits** - selection of data is followed by entries for the minimum and maximum data limits; the defaults are taken from the data Limits imposed on the original PWDR data or the r-range for the PDF G(r) data. The units are degrees \(2\theta\), TOF in μs, or Å, as appropriate. Refer to any PWDR (or PDF) plot to select these values; leading background should be skipped, and the upper limit chosen from a relatively clear point where there are still significant peaks. Values will be used to give the cluster analysis input data matrix size.
* **Make Cluster Analysis data array** - this button forms the data matrix for cluster analysis; it is number of data sets times number of data points between the limits in size. the next item will appear in the GUI.
* **Select cluster analysis distance method** - there are several choices as what is meant by "distance" between all pairwise selection of data vectors (u & v). They are (as taken from scipy):

    * **braycurtis** – Computes the Bray-Curtis distance between the data vectors as

    $$
    d(u,v) = \frac{\sum_i | u_i - v_i | }{\sum_i | u_i + v_i |}
    $$

    * **canberra** – Computes the Canberra distance between data vectors as:

    $$
    d(u,v) = \sum {\frac{ | u_i - v_i | }{| u_i | + |v_i |} }
    $$

    * **chebyschev** – Computes the Chebyschev distance between data vectors as:

    $$
    d(u,v) = \max { | u_i - v_i | }
    $$

    * **cityblock** (sometimes called "Manhattan") – Computes the city block distance between data vectors as:

    $$
    d(u,v) = \sum { | u_i - v_i | }
    $$

    * **correlation** – Computes the correlation distance between data vectors as:

    $$
    d(u,v) = 1 - \frac{ ( u - \bar{u} ) \cdot ( v - \bar{v} ) }{ \sqrt{ ( u - \bar{u} )^2 ( v - \bar{v} )^2}}
    $$

    * **cosine** – Computes the cosine squared between the data vectors as:

    $$
    d(u,v) = 1 - \frac{ u \cdot v }{ \sqrt{ u^2 v^2 } }
    $$

    *  **euclidian** (default) – Computes the Euclidian distance between the data vectors as:

    $$
    d(u,v) = \sqrt{ \sum_i ( u_i - v_i )^2 }
    $$

    * **jensenshannon** – Computes the Jensen-Shannon distance between the data vectors

    * **minkowski** – Computes the Minkowski distance between the data vectors as:

    $$
    d(u,v) = \sqrt[p]{ \sum_i {| u_i - v_i |^p } }
    $$

    where the exponent, p, = 2 by default; this is identical to the Euclidian formula. Some choices for p: 1 is the same as city block, and 10 (~  ∞) is essentially the same as Chebyschev. The others (3 & 4) give distance results that are between Euclidian (p=2) and Chebyschev (p=10 ~ ∞).

    * **seculidian** – Computes the standardized Euclidian distance between the data vectors as:

    $$
    d(u,v) = \sqrt{ \sum_i {( u_i - v_i )^2 }/V[x_i] }
    $$

    where the variance, \(V[x_i]\), is computed automatically as the variance in the data point values for each data position (i.e. \(2\theta\)) across the entire data array.

    * **sqeuclidian** – Computes the squared Euclidian distance between the data vectors as:

    $$
    d(u,v) =  \sum_i {( u_i - v_i )^2 }
    $$

Changing the method results in an automatic calculation of the distances; the Compute button is provided for convenience. The result of this calculation is displayed as the 1st plot in a plot tab named for the selected distance method; this facilitates comparison between methods for your data. Also shown in this plot tab is a 3D plot of the result of a Principal Component Analysis (PCA) of the distance data; it shows the location of each data set in this space. Clusters may be evident from this plot; variable temperature scans tend to show a complex path of distance points with cluster grouping corresponding to phases. Since data sets may be in a series, a plot of the serial distances across the suite of data is shown; spikes in a temperature series may indicate phase changes. The GUI will be extended to show more steps in cluster analysis.

* **linkage method for hierarchical clustering** - there are several choices for linkage in determining the hierarchical relationship (if any) between the data sets and the algorithm will use the distance matrix determined above to determine the data hierarchy. The distances are used by the linkage method to group similar data into clusters; these are successively combined until just a single cluster is obtained. A dendrogram is displayed showing the progression of this clustering. Each cluster is given a mean position, s or t, to compare to the others. The linkage methods for calculating the distance (using the distance method, dist, as selected above) between each pair of clusters are:

    * **single** – computes the linkage as:

    $$
    d(s,t) = \min(dist(u(s)_i,v(t)_j))
    $$

    * **complete** – computes the linkage as:

    $$
    d(s,t) = \max(dist(u(s)_i,v(t)_j)
    $$

    * **average** (default) – computes the linkage as (Ns, Nt are numbers of members in cluster s & t, respectively):

    $$
    d(s,t) = \sum_{ij} {\frac{  dist(u(s)_i,v(t)_j)}{N_s N_t}}
    $$

    * **weighted** – computes the linkage when s is formed with clusters u & v and t is another cluster as:

    $$
    d(s,t) = (dist(u,t)+dist(v,t))/2
    $$

    * **centroid** ("UPGMC") – computes the linkage when cs & ct are the centroids of clusters s & t, respectively as:

    $$
    d(s,t) = (dist(c_s, c_t)
    $$

    * **median** ("WPGMC") – computes the linkage when ms & mt are the medians for all member pairs in clusters s & t as:

    $$
    d(s,t) = (dist(m_s, m_t)
    $$

    * **ward** – computes the linkage when s is formed with clusters u & v and t is another cluster as (Nu, Ns, Nt are numbers of members in cluster u, s & t, respectively, & T=Nu+Nv+Nt):

    $$
    d(s,t) = \sqrt{ \frac{N_t+N_u}{T}dist^2(t,u) + \frac{N_t+N_v}{T} dist^2(t,v) - \frac{N_t}{T} dist^2(u,v) } 
    $$

    Changing the linkage method results in an automatic recalculation of the hierarchical clustering; a Compute button is provided for convenience. The result of this calculation is shown as a dendrogram in the same plot tab; the 4th plot shows the percentage contribution of the leading terms in the PCA to the distance data. Usually, 2-3 terms are sufficient to describe the distribution.

* **Select number of clusters** for K-means clustering (scipy algorithm). The algorithm attempts to group the data points (e. g. as in the PCA plot) into the requested number of clusters based on Euclidian distances on a "whitened" data array (i. e. not the distance matrix). To whiten the data matrix the suite of values at each position (e. g. at each \(2\theta\)) are divided by its standard deviation; this reduces the scale of the PWDR & PDF observations to just numbers of standard deviations from zero. Use the Compute to repeat the K-means clustering; the start points are randomly selected and will sometimes yield different results. Cluster populations are shown in the GUI, clusters are colored to match the data point colors in the PCA plot.

    * **Select cluster to list members** – Shows a colored list of the data items that belong to the selected cluster.
    * **Select cluster member** (use mouse RB on item in displayed list) – Displays the PWDR (or PDF) data on the Powder Pattern plot tab for the selected item.

<a name="Cluster-PlotSel"></a>
* **Plot selection** – changes the displayed plots:
    * **All** – All four plots are shown
    * **Distances** – Only the distance matrix is shown
    * **Dendogram** – Only the hierarchical dendrogram is shown.
    * **3D-PCA** – Only the 3D representation of the Principal Component Analysis is shown.
    * **Diffs** – Only the serial differences are shown.

## Cluster Analysis with scikit-learn

The next section of the GUI only appears if the scikit-learn package is installed. It has multiple algorithms for doing clustering and detecting outliers (i. e. bad data) in the suite of PWDR or PDF patterns. Changing the method or number of clusters results in an automatic calculation; the **Compute** button is provided for convenience. There is a reminder to properly cite Scikit-learn if you use it.

* **Select clustering method** – some may also require selecting number of clusters

    * **K-Means** (requires number of clusters) – Uses the scikit-learn "K-means++" algorithm for clustering; this gives a better starting position and usually succeeds on the 1st try. It uses the "whitened" data matrix.
    * **Affinity propagation** – It uses the distance matrix computed above.
    * **Mean-shift** – It uses the "whitened" data matrix.
    * **Spectral clustering** (requires number of clusters) – It uses the "whitened" data matrix.
    * **Agglomerative clustering** (requires number of clusters) – It uses the distance matrix computed above.

For details of these methods, please see [2.3. Clustering — scikit-learn 1.1.2 documentation](https://scikit-learn.org/stable/modules/clustering.html). After completion, Cluster populations are shown in the GUI and clusters are colored to match the data point colors in the PCA plot.

## Outlier Analysis with scikit-learn

After selection of the PWDR or PDF data and doing the distance calculation, one can examine the distance data for possible "bad" data items. These outliers can be detected by a choice of methods that make different assumptions how the data "should" be clustered; any data that do not fall within them are flagged as outliers and are colored different in the resulting 3D PCA plot from all others that would be in clusters. Although the chosen distance method affects the appearance of the 3D PCA plot, the three outlier methods all use the original data, thus are independent of any selected distance method. The GUI is refreshed showing a listing of the outlier data; selection of any, displays that data item in the powder pattern plot tab. Any previous cluster identification, e. g. by K-means, is erased. The outlier detection methods are:

* **One-Class SVM** - Attempts to form boundaries around the clusters; outliers are items that fall outside the boundaries.
* **Isolation Forest** - Similar to the above but uses a different algorithm.
* **Local Outlier Factor** - Uses the local density of other points about each point to determine if it is within a high-density area, i. e. in a cluster, or not.

Further details of these methods can be found at [2.7. Novelty and Outlier Detection — scikit-learn 1.1.2 documentation](https://scikit-learn.org/stable/modules/outlier_detection.html). The current GSAS-II implementation of these methods all use the default settings for any of their respective parameters.

<H3 style="color:blue;font-size:1.1em">What can I do with the plots?</H3>

For each selection of distance method, i.e. "Euclidian", a plot tab is created with 2 or 4 plots. They are: 

1. the distance matrix displayed in the same way the refinement covariance matrix is displayed (default coloring is "paired" – same parameter as the powder pattern contour plot); 
2. the 3D PCA analysis plot; 
3. the hierarchical dendrogram plot and 
4. the PCA percent contribution plot. 

Each can be zoomed independent of the others and the 1st three can be selected to show as a single plot in the tab (see [**Plot selection**, above](#Cluster-PlotSel)). A LB mouse selection (& hold button down) of a 3D PCA point will show the data set name in the plot status line. If clusters are determined by e. g. K-means, the 3D PCA points will be colored by cluster membership.

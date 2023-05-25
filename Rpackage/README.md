<!-- README.md is generated from the source: README.Rmd -->

# Empirical Bayesian Lasso and Elastic Net Methods for Generalized Linear Models <img src="man/figures/logo.png" width="100" align="right" />

[![CRAN_Status_Badge](https://www.r-pkg.org/badges/version/EBglmnet)](https://cran.r-project.org/package=EBglmnet)[![](https://cranlogs.r-pkg.org/badges/EBglmnet)](https://CRAN.R-project.org/package=EBglmnet)

We provide extremely efficient procedures for fitting the empirical
Bayesian methods with lasso and elastic net hierarchical priors for
linear regression (gaussian), and logistic regression (binomial) models.
Key features include sparse variable selection and effect estimation via
generalized linear regression models, high dimensionality with p\>\>n,
and significance test (with output of `p-value`) for nonzero effects.
The algorithm uses a closed-form solution for Bayesian variance
estimation in an iterative cooridinate descent algorithm estimating the
Bayesian means implemented with BLAS/Lapack routines. The implementation
enables extremely efficient computation comparable with that of `glmnet`
package. Details may be found in Huang A. and Liu D
([2016](#ref-package)), Huang A., Xu S., and Cai X. ([2015](#ref-EBEN)),
Huang A. ([2014](#ref-dissertation)), Huang A., Xu S., and Cai X.
([2013](#ref-EBlasso)), and Cai X., Huang A., and Xu S.,
([2011](#ref-QTL)).

Version 6.0 is a major release with several new features, including:

- simplified user interface with central functions and simple parameters
  setup;
- generalized documentation language to avoid confusion of different use
  cases;
- group Empirical Bayesian Lasso (EBlasso) and built-in two-way
  interaction support moved to `EBEN` package.

Version 5.0 is a major release that updates BLAS/Lapack routines
according to R-API change.

## References

<div id="refs" class="references">

<div id="ref-package">

<p>
Huang A., Liu D., (2016) <br> EBglmnet: a comprehensive R package for
sparse generalized linear regression models <br> Bioinformatics, Volume
37, Issue 11, Pages 1627–1629
</p>

</div>

<div id="ref-EBEN">

<p>
Huang A., Xu S., and Cai X. (2015). <br> Empirical Bayesian elastic net
for multiple quantitative trait locus mapping.</a><br>
<em>Heredity</em>, Vol. 114(1), 107-115.
</p>

</div>

<div id="ref-dissertation">

<p>
Huang A. (2014) <br> Sparse Model Learning for Inferring Genotype and
Phenotype Associations. <br> Ph.D Dissertation, University of Miami,
Coral Gables, FL, USA.
</p>

</div>

<div id="ref-EBlasso">

<p>
Huang A., Xu S., and Cai X. (2013). <br> Empirical Bayesian
LASSO-logistic regression for multiple binary trait locus mapping.
</a><br> <em>BMC Genetics</em>, 14(1),5.
</p>

</div>

<div id="ref-QTL">

<p>
Cai X., Huang A., and Xu S., (2011). <br> Fast empirical Bayesian LASSO
for multiple quantitative trait locus mapping. </a><br> <em>BMC
Bioinformatics</em>, 12(1),211.
</p>

</div>

</div>

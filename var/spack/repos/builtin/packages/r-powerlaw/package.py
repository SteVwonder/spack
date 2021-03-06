# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RPowerlaw(RPackage):
    """An implementation of maximum likelihood estimators for a variety of
       heavy tailed distributions, including both the discrete and continuous
       power law distributions. Additionally, a goodness-of-fit based approach
       is used to estimate the lower cut-off for the scaling region."""

    homepage = "https://github.com/csgillespie/poweRlaw"
    url      = "https://cran.rstudio.com/src/contrib/poweRlaw_0.70.1.tar.gz"
    list_url = "https://cran.rstudio.com/src/contrib/Archive/poweRlaw"

    version('0.70.1', '4117cb95c37f72441f320ea12f553065')

    depends_on('r-vgam', type=('build', 'run'))

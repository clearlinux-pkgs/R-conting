#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-conting
Version  : 1.7
Release  : 26
URL      : https://cran.r-project.org/src/contrib/conting_1.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/conting_1.7.tar.gz
Summary  : Bayesian Analysis of Contingency Tables
Group    : Development/Tools
License  : GPL-2.0
Requires: R-BMS
Requires: R-coda
Requires: R-gtools
Requires: R-mvtnorm
Requires: R-tseries
BuildRequires : R-BMS
BuildRequires : R-coda
BuildRequires : R-gtools
BuildRequires : R-mvtnorm
BuildRequires : R-tseries
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n conting
cd %{_builddir}/conting

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589770580

%install
export SOURCE_DATE_EPOCH=1589770580
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library conting
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library conting
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library conting
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc conting || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/conting/DESCRIPTION
/usr/lib64/R/library/conting/INDEX
/usr/lib64/R/library/conting/Meta/Rd.rds
/usr/lib64/R/library/conting/Meta/data.rds
/usr/lib64/R/library/conting/Meta/features.rds
/usr/lib64/R/library/conting/Meta/hsearch.rds
/usr/lib64/R/library/conting/Meta/links.rds
/usr/lib64/R/library/conting/Meta/nsInfo.rds
/usr/lib64/R/library/conting/Meta/package.rds
/usr/lib64/R/library/conting/NAMESPACE
/usr/lib64/R/library/conting/R/conting
/usr/lib64/R/library/conting/R/conting.rdb
/usr/lib64/R/library/conting/R/conting.rdx
/usr/lib64/R/library/conting/data/AOH.rda
/usr/lib64/R/library/conting/data/ScotPWID.rda
/usr/lib64/R/library/conting/data/heart.rda
/usr/lib64/R/library/conting/data/spina.rda
/usr/lib64/R/library/conting/help/AnIndex
/usr/lib64/R/library/conting/help/aliases.rds
/usr/lib64/R/library/conting/help/conting.rdb
/usr/lib64/R/library/conting/help/conting.rdx
/usr/lib64/R/library/conting/help/paths.rds
/usr/lib64/R/library/conting/html/00Index.html
/usr/lib64/R/library/conting/html/R.css

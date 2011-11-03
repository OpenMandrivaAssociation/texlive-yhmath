# revision 15878
# category Package
# catalog-ctan /fonts/yhmath
# catalog-date 2007-03-01 23:46:20 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-yhmath
Version:	20070301
Release:	1
Summary:	Extended maths fonts for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/yhmath
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yhmath.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yhmath.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yhmath.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The yhmath bundle contains fonts (type in 1 format) and a LaTeX
package for using them.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/yhmath/yhmath.map
%{_texmfdistdir}/fonts/source/public/yhmath/yhbigacc.mf
%{_texmfdistdir}/fonts/source/public/yhmath/yhbigdel.mf
%{_texmfdistdir}/fonts/source/public/yhmath/yhcmex10.mf
%{_texmfdistdir}/fonts/source/public/yhmath/yhmathex.mf
%{_texmfdistdir}/fonts/source/public/yhmath/yrcmex10.mf
%{_texmfdistdir}/fonts/tfm/public/yhmath/yhcmex10.tfm
%{_texmfdistdir}/fonts/tfm/public/yhmath/yrcmex10.tfm
%{_texmfdistdir}/fonts/type1/public/yhmath/yhcmex.pfb
%{_texmfdistdir}/fonts/vf/public/yhmath/yhcmex10.vf
%{_texmfdistdir}/tex/latex/yhmath/OMXyhex.fd
%{_texmfdistdir}/tex/latex/yhmath/yhmath.sty
%doc %{_texmfdistdir}/doc/latex/yhmath/yhmath.pdf
#- source
%doc %{_texmfdistdir}/source/latex/yhmath/yhmath.drv
%doc %{_texmfdistdir}/source/latex/yhmath/yhmath.dtx
%doc %{_texmfdistdir}/source/latex/yhmath/yhmath.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

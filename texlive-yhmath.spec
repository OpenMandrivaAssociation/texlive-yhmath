Name:		texlive-yhmath
Epoch:		1
Version:	54377
Release:	1
Summary:	Extended maths fonts for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/yhmath
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yhmath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yhmath.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yhmath.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The yhmath bundle contains fonts (in type 1 format) and a LaTeX
package for using them.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/yhmath
%{_texmfdistdir}/fonts/source/public/yhmath
%{_texmfdistdir}/fonts/tfm/public/yhmath
%{_texmfdistdir}/fonts/type1/public/yhmath
%{_texmfdistdir}/fonts/vf/public/yhmath
%{_texmfdistdir}/tex/latex/yhmath
%doc %{_texmfdistdir}/doc/fonts/yhmath
#- source
%doc %{_texmfdistdir}/source/fonts/yhmath

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}

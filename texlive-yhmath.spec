%global tl_name yhmath
%global tl_revision 77682
%global tl_version 1.6

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Extended maths fonts for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/yhmath
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yhmath.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yhmath.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yhmath.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The yhmath bundle contains fonts (in Metafont and type 1 format) and a
LaTeX package for using them.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from yhmath:
MixedMap yhmath.map
TL_DROPIN_EOF

Name:		texlive-fcolumn
Version:	61855
Release:	1
Summary:	Typesetting financial tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fcolumn
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fcolumn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fcolumn.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fcolumn.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
In financial reports, text and currency amounts are regularly
put in one table, e.g., a year balance or a profit-and-loss
overview. This package provides the settings for automatically
typesetting such columns, including the sum line (preceded by a
rule of the correct width) using the specifier "f".

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/fcolumn
%{_texmfdistdir}/tex/latex/fcolumn
%doc %{_texmfdistdir}/doc/latex/fcolumn

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

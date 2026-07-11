%global tl_name fcolumn
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Typesetting financial tables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fcolumn
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fcolumn.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fcolumn.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fcolumn.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
In financial reports, text and currency amounts are regularly put in one
table, e.g., a year balance or a profit-and-loss overview. This package
provides the settings for automatically typesetting such columns,
including the sum line (preceded by a rule of the correct width) using
the specifier "f".


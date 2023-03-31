Name:		fonts-ttf-arimo
Version:	1.0
Release:	2
Summary:	Arimo ttf fonts
License:	Apache License v2.00
Group:		System/Fonts/True type
Url:		https://www.ascenderfonts.com/
Source0:	%{name}-%version.tar.gz
BuildArch:	noarch

%description
Arimo is a typeface which is metrics compatible with Arial.

%files
%dir %{_datadir}/fonts/TTF/arimo/
%{_datadir}/fonts/TTF/arimo/*

%prep
%setup -qn %{name}-%{version}/fonts/TTF/arimo/

%build
#

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/arimo
install -Dm 644  *.ttf  %{buildroot}%{_datadir}/fonts/TTF/arimo/

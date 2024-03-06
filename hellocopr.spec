%global srcname copr-tito-quickdoc

Name: hellocopr
Version: 1.0.5
Release: 1%{?dist}
License: GPLv3
Summary: A trivial python 3 program for demonstrating RPM packaging
Url: https://pagure.io/%{srcname}
# Sources can be obtained by
# git clone https://pagure.io/copr-tito-quickdoc
# cd copr-tito-quickdoc
# tito build --tgz
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

%if 0%{?el6}
BuildRequires: python34-devel
BuildRequires: python34-setuptools
%else
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%endif

%description
Hellocopr is a very simple demonstration program that does nothing but display
some text on the command line. It is used as an example for automatic RPM
packaging using tito and Fedora's Copr user repository.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup

%build
%py3_build

%install
%py3_install

#-- FILES ---------------------------------------------------------------------#
%files
%doc README.md
%license LICENSE
%{_bindir}/hellocopr
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Wed Mar 06 2024 Wheeler Law <wheeler.law@outlook.com>
- new package built with tito

* Wed Mar 06 2024 Wheeler Law <wheeler.law@outlook.com>
- new package built with tito

* Wed Mar 06 2024 Wheeler Law <wheeler.law@outlook.com>
- new package built with tito

* Wed Mar 06 2024 Wheeler Law <wheeler.law@outlook.com>
- new package built with tito


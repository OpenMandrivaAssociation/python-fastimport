%global module_name fastimport

Name:           python-%{module_name}
Version:        0.9.14
Release:        2
Summary:        Python parser for fastimport (VCS interchange format)
License:        GPLv2+
URL:            https://launchpad.net/python-fastimport
Source0:        https://files.pythonhosted.org/packages/source/f/%{module_name}/%{module_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose

%description
This is the Python parser that was originally developed for bzr-fastimport, but 
extracted so it can be used by other projects.

%prep
%setup -q -n %{module_name}-%{version}
# Fix shebangs
sed -i -e 's@^#!/usr/bin/python@#!%{__python3}@' bin/*

%build
%{py_build}

%install
%{py_install}

%check
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitelib} %{_bindir}/nosetests-3 %{module_name}

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{python_sitelib}/%{module_name}*
%{_bindir}/fast-import-filter
%{_bindir}/fast-import-info
%{_bindir}/fast-import-query


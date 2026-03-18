%define module fastimport
%bcond tests 1

Name:		python-fastimport
Version:	0.9.16
Release:	1
Summary:	Python parser for fastimport (VCS interchange format)
License:	GPL-2.0-or-later
Group:		Development/Python
URL:		https://github.com/jelmer/python-fastimport
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:      noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
This is the Python parser that was originally developed for bzr-fastimport, but 
extracted so it can be used by other projects.

%prep -a
# Fix shebangs
sed -i -e 's@^#!/usr/bin/python@#!%{__python3}@' bin/*

%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python} -m unittest
%endif

%files
%doc AUTHORS README.md
%license COPYING
%{_bindir}/fast-import-filter
%{_bindir}/fast-import-info
%{_bindir}/fast-import-query
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info


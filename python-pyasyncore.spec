%define module pyasyncore
%bcond tests 1

Name:		python-pyasyncore
Summary:	Make asyncore available for Python 3.12 onwards
Version:	1.0.5
Release:	1
License:	PSF-2.0
Group:		Development/Python
URL:		https://github.com/simonrob/pyasyncore
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(setuptools)
%if %{with tests}
BuildRequires:	python-test
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
This package contains the asyncore module as found in Python versions prior
to 3.12.

It is provided so that existing code relying on import asyncore is able to
continue being used without significant refactoring.

Please note that new projects should prefer to use the Python standard
library's asyncio library.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info
# lets not publish executable documents
chmod -x LICENSE README.md

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest -rs
%endif

%files
%doc README.md
%license LICENSE
%{python_sitelib}/asyncore
%{python_sitelib}/%{module}-%{version}*.*-info

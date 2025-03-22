#
# Conditional build:
%bcond_with	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		css_parser
%define		egg_name	css_parser
%define		pypi_name	css-parser
Summary:	A CSS Cascading Style Sheets library for Python
Name:		python-%{module}
Version:	1.0.9
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	9af58609a009baa3ce606779daefb615
URL:		https://pypi.org/project/css-parser/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fork of the cssutils project based on version 1.0.2. This fork
includes general bug fixes and extensions specific to editing and
working with ebooks.

%package -n python3-%{module}
Summary:	A CSS Cascading Style Sheets library for Python
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
A fork of the cssutils project based on version 1.0.2. This fork
includes general bug fixes and extensions specific to editing and
working with ebooks.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

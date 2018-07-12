%global pypi_name XStatic-Angular-UUID

Name:           python-%{pypi_name}
Version:        0.0.4.0
Release:        0%{?dist}
Provides:       python2-XStatic-Angular-UUID = %{version}-%{release}
Summary:        Angular-UUID (XStatic packaging standard)

License:        MIT
URL:            https://github.com/munkychop/angular-uuid
Source0:        https://files.pythonhosted.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  web-assets-devel

Requires:       web-assets-filesystem
Requires:       python-XStatic


%description
Angular-UUID JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/angular_uuid'|" xstatic/pkg/angular_uuid/__init__.py

%build
# due
# https://bitbucket.org/thomaswaldmann/xstatic/issue/2/
# this package can not be built with python-XStatic installed.
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}/%{_jsdir}/angular_uuid
mv %{buildroot}/%{python2_sitelib}/xstatic/pkg/angular_uuid/data/angular-uuid.js %{buildroot}/%{_jsdir}/angular_uuid
rmdir %{buildroot}%{python2_sitelib}/xstatic/pkg/angular_uuid/data/



%files
%doc README.txt
%{python2_sitelib}/xstatic/pkg/angular_uuid
%{python2_sitelib}/XStatic_Angular_UUID-%{version}-py%{python_version}.egg-info
%{python2_sitelib}/XStatic_Angular_UUID-%{version}-py%{python_version}-nspkg.pth
%{_jsdir}/angular_uuid

%changelog
* Thu Jul 12 2018 Radomir Dopieralski <rdopiera@redhat.com) - 0.0.4.0-0
- Initial package

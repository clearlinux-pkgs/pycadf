#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycadf
Version  : 2.4.0
Release  : 28
URL      : http://tarballs.openstack.org/pycadf/pycadf-2.4.0.tar.gz
Source0  : http://tarballs.openstack.org/pycadf/pycadf-2.4.0.tar.gz
Summary  : CADF Library
Group    : Development/Tools
License  : Apache-2.0
Requires: pycadf-python
Requires: pycadf-data
BuildRequires : Jinja2
BuildRequires : Sphinx-python
BuildRequires : coverage-python
BuildRequires : debtcollector-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : flake8-docstrings-python
BuildRequires : funcsigs-python
BuildRequires : imagesize-python
BuildRequires : msgpack-python-python
BuildRequires : oslo.config
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyrsistent-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : setuptools
BuildRequires : testrepository-python
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : virtualenv
Patch1: 0001-test.patch

%description
======
PyCADF
======
.. image:: https://img.shields.io/pypi/v/pycadf.svg
:target: https://pypi.python.org/pypi/pycadf/
:alt: Latest Version

%package data
Summary: data components for the pycadf package.
Group: Data

%description data
data components for the pycadf package.


%package python
Summary: python components for the pycadf package.
Group: Default
Requires: debtcollector-python
Requires: oslo.config
Requires: oslo.serialization-python
Requires: pytz-python

%description python
python components for the pycadf package.


%prep
%setup -q -n pycadf-2.4.0
%patch1 -p1

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
## make_install_append content
install -d -m 755 %{buildroot}/usr/share/defaults/pycadf
mv %{buildroot}/usr/etc/pycadf/* %{buildroot}/usr/share/defaults/pycadf
rm -rf %{buildroot}/usr/etc
## make_install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/defaults/pycadf/ceilometer_api_audit_map.conf
/usr/share/defaults/pycadf/cinder_api_audit_map.conf
/usr/share/defaults/pycadf/glance_api_audit_map.conf
/usr/share/defaults/pycadf/neutron_api_audit_map.conf
/usr/share/defaults/pycadf/nova_api_audit_map.conf
/usr/share/defaults/pycadf/trove_api_audit_map.conf

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

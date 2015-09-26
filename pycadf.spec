#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycadf
Version  : 1.1.0
Release  : 15
URL      : http://tarballs.openstack.org/pycadf/pycadf-1.1.0.tar.gz
Source0  : http://tarballs.openstack.org/pycadf/pycadf-1.1.0.tar.gz
Summary  : CADF Library
Group    : Development/Tools
License  : Apache-2.0
Requires: pycadf-python
Requires: pycadf-data
BuildRequires : Babel-python
BuildRequires : Jinja2-python
BuildRequires : PyYAML-python
BuildRequires : Pygments-python
BuildRequires : Sphinx-python
BuildRequires : WebOb-python
BuildRequires : aioeventlet-python
BuildRequires : amqp-python
BuildRequires : anyjson-python
BuildRequires : coverage-python
BuildRequires : debtcollector-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : eventlet-python
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : futures-python
BuildRequires : greenlet-python
BuildRequires : hacking-python
BuildRequires : iso8601-python
BuildRequires : kombu-python
BuildRequires : linecache2-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : monotonic-python
BuildRequires : mox3-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr-python
BuildRequires : netifaces-python
BuildRequires : oslo.config-python
BuildRequires : oslo.context-python
BuildRequires : oslo.i18n-python
BuildRequires : oslo.messaging-python
BuildRequires : oslo.middleware-python
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8-python
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse
BuildRequires : python-mock
BuildRequires : python-subunit-python
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore-python
BuildRequires : testrepository-python
BuildRequires : testscenarios-python
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : trollius-python
BuildRequires : unittest2-python
BuildRequires : virtualenv
BuildRequires : wrapt-python

%description
======
PyCADF
======
This library provides an auditing data model based on the `Cloud Auditing Data
Federation <http://www.dmtf.org/standards/cadf>`_ specification, primarily for
use by OpenStack. The goal is to establish strict expectations about what
auditors can expect from audit notifications.

%package data
Summary: data components for the pycadf package.
Group: Data

%description data
data components for the pycadf package.


%package python
Summary: python components for the pycadf package.
Group: Default

%description python
python components for the pycadf package.


%prep
%setup -q -n pycadf-1.1.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
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

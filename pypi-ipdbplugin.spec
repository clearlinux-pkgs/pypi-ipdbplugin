#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ipdbplugin
Version  : 1.5.0
Release  : 33
URL      : https://files.pythonhosted.org/packages/cf/cb/510dcb9ae401e6876415412f0cc7bd2df8f7e9eb6667c23a2bd941309b88/ipdbplugin-1.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/cf/cb/510dcb9ae401e6876415412f0cc7bd2df8f7e9eb6667c23a2bd941309b88/ipdbplugin-1.5.0.tar.gz
Summary  : Nose plugin to use iPdb instead of Pdb when tests fail
Group    : Development/Tools
License  : LGPL-2.1
Requires: pypi-ipdbplugin-python = %{version}-%{release}
Requires: pypi-ipdbplugin-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(ipython)
BuildRequires : pypi(nose)

%description
Use this and *never* risk yourself forgetting `import ipdb; ipdb.set_trace()` in your code again!
        
                This plugin is 99.99% based on nose's builtin debug plugin.

%package python
Summary: python components for the pypi-ipdbplugin package.
Group: Default
Requires: pypi-ipdbplugin-python3 = %{version}-%{release}

%description python
python components for the pypi-ipdbplugin package.


%package python3
Summary: python3 components for the pypi-ipdbplugin package.
Group: Default
Requires: python3-core
Provides: pypi(ipdbplugin)
Requires: pypi(ipython)
Requires: pypi(nose)

%description python3
python3 components for the pypi-ipdbplugin package.


%prep
%setup -q -n ipdbplugin-1.5.0
cd %{_builddir}/ipdbplugin-1.5.0
pushd ..
cp -a ipdbplugin-1.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656399401
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

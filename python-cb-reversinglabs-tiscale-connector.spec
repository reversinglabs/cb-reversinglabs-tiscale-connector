%define name python-cb-reversinglabs-tiscale-connector
%define version 1.0
%define unmangled_version 1.0
%define release 2
%define __prelink_undo_cmd %{nil}
%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Summary: Carbon Black reversinglabs Bridge
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64
Vendor: Carbon Black
Url: http://www.carbonblack.com/

%description
UNKNOWN

%prep
%setup -n %{name}-%{unmangled_version}

%build
pyinstaller cb-reversinglabs-tiscale-connector.spec

%install
python setup.py install_cb --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%posttrans
mkdir -p /usr/share/cb/integrations/reversinglabs-tiscale/db
mkdir -p /var/log/cb/integrations/reversinglabs-tiscale
chkconfig --add cb-reversinglabs-tiscale-connector
chkconfig --level 345 cb-reversinglabs-tiscale-connector on

# not auto-starting because conf needs to be updated
#/etc/init.d/cb-reversinglabs-tiscale-connector start


%preun
/etc/init.d/cb-reversinglabs-tiscale-connector stop

# only delete the chkconfig entry when we uninstall for the last time,
# not on upgrades
if [ "X$1" = "X0" ]
then
    chkconfig --del cb-reversinglabs-tiscale-connector
fi


%files -f INSTALLED_FILES
%defattr(-,root,root)

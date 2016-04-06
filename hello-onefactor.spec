Name: 		hello-onefactor
Version: 	0.0.3
Release:	1
Summary:	Hello OneFactor

Group:		Applications/System
License:	Some Licence
URL:		https://github.com/meshok0/hello-onefactor/
Source0:	%{name}-%{version}.tar.gz

BuildArch:	noarch

Requires:	java-1.7.0-openjdk	

%define __jar_repack %{nil}

%description
Test task for OneFactor


%prep
%setup -q


%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib
mkdir -p $RPM_BUILD_ROOT/etc/systemd/system
cp usr/lib/hello-onefactor.jar $RPM_BUILD_ROOT/usr/lib/
cp etc/systemd/system/hello-onefactor.service $RPM_BUILD_ROOT/etc/systemd/system/

%clean

%files
%defattr(-,root,root,-)
/usr/lib/hello-onefactor.jar
/etc/systemd/system/hello-onefactor.service

%doc


%changelog


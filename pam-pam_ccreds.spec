%define 	modulename pam_ccreds
Summary:	PAM cached credentials module
Name:		pam-%{modulename}
Version:	4
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.padl.com/download/pam_ccreds-%{version}.tar.gz
# Source0-md5:	7dfba0860195d63e173bdb08450462d7
URL:		http://www.padl.com/OSS/pam_ccreds.html
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pam_ccreds module provides the means for Linux workstations to
locally authenticate using an enterprise identity when the network is
unavailable. Used in conjunction with the nss_updatedb utility, it
provides a mechanism for disconnected use of network directories. They
are designed to work with pam_ldap and nss_ldap

%prep
%setup -q -n %{modulename}-%{version}

%build
%{__autoconf}
%{__autoheader}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}/security
install pam_ccreds.so $RPM_BUILD_ROOT/%{_lib}/security

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS COPYING README ChangeLog
%attr(755,root,root) /%{_lib}/security/pam_ccreds.so

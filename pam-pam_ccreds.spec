%define 	modulename pam_ccreds
Summary:	PAM cached credentials module
Summary(pl.UTF-8):	Moduł PAM do zapamiętywania danych uwierzytelniających
Name:		pam-%{modulename}
Version:	10
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.padl.com/download/pam_ccreds-%{version}.tar.gz
# Source0-md5:	21b008071ee8bfb998bd499c0fa92ba1
URL:		http://www.padl.com/OSS/pam_ccreds.html
BuildRequires:	autoconf
BuildRequires:	db-devel
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pam_ccreds module provides the means for Linux workstations to
locally authenticate using an enterprise identity when the network is
unavailable. Used in conjunction with the nss_updatedb utility, it
provides a mechanism for disconnected use of network directories. They
are designed to work with pam_ldap and nss_ldap.

%description -l pl.UTF-8
Moduł pam_ccreds umożliwia stacjom linuksowym na lokalne
uwierzytelnianie przy użyciu firmowej tożsamości podczas
niedostępności sieci. Używany w połączeniu z narzędziem nss_updatedb
udostępnia mechanizm do używania katalogów sieciowych przy braku
połączenia. Narzędzia te są zaprojektowane do użytku z pam_ldap i
nss_ldap.

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) /%{_lib}/security/pam_ccreds.so

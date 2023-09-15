#
%define		packagename		py-smbpasswd
#
Summary:	Python SMB Password Hash Generator module
Summary(pl.UTF-8):	Moduł języka Python kodujący hasła funkcją zgodną z SMB
Name:		python-smbpasswd
Version:	1.0.1
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	http://barryp.org/static/software/download/%{packagename}/%{version}/%{packagename}-%{version}.tar.gz
# Source0-md5:	0eab2c29588e32e77ce6e5d2faea7874
URL:		http://barryp.org/software/py-smbpasswd/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Obsoletes:	py-smbpasswd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python SMB Password Hash Generator module that can generate both
LANMAN and NT password hashes, suitable for use with Samba.

%description -l pl.UTF-8
Moduł języka Python kodujący hasła funkcją zgodną z hasłami LANMAN
oraz NT do wykorzystania w sieciach SMB.

%prep
%setup -q -n %{packagename}-%{version}

%build
find -type f -exec sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g' "{}" ";"
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt CHANGES.txt
%attr(755,root,root) %{py_sitedir}/*.so

#
%define		packagename		py-smbpasswd
#
Summary:	Python SMB Password Hash Generator module
Summary(pl.UTF-8):	Moduł języka Python kodujący hasła funkcją zgodną z SMB
Name:		python-smbpasswd
Version:	1.0.1
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://barryp.org/static/software/download/%{packagename}/%{version}/%{packagename}-%{version}.tar.gz
# Source0-md5:	0eab2c29588e32e77ce6e5d2faea7874
URL:		http://barryp.org/software/py-smbpasswd/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
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
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

python ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt CHANGES.txt
%attr(755,root,root) %{py_sitedir}/*.so

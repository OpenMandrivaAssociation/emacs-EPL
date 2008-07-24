%define version 0.7
%define name emacs-EPL
%define release  %mkrel 9


Summary: Control Emacs using Perl as an alternative to Emacs Lisp
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Development/Perl
Source: http://www.cpan.org/modules/by-module/Emacs/Emacs-EPL-%{version}.tar.bz2
Requires: emacs, perl
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch

%description
EPL (Emacs Perl) lets you control Emacs and XEmacs using Perl as an alternative
to Emacs Lisp.

%prep
%setup -n Emacs-EPL-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
(
 cd lisp
 for i in *.el; do install -D $i $RPM_BUILD_ROOT/usr/share/emacs/site-lisp/$i; done
)

install -d $RPM_BUILD_ROOT/etc/emacs/site-start.d
echo "(require 'perl)" > $RPM_BUILD_ROOT/etc/emacs/site-start.d/epl.el

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Emacs*
%_mandir/*/*
%{_datadir}/emacs/site-lisp/*
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/*


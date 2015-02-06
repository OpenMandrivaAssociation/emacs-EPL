%define version 0.7
%define name emacs-EPL
%define release  11


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



%changelog
* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.7-10mdv2010.0
+ Revision: 428557
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.7-9mdv2009.0
+ Revision: 244699
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.7-7mdv2008.1
+ Revision: 136403
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - fix installing
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - fix summary-ended-with-dot
    - import emacs-EPL


* Fri Apr 29 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.7-7mdk
- rebuild for new emacs

* Fri Jun  4 2004 Pixel <pixel@mandrakesoft.com> 0.7-6mdk
- rebuild

* Fri Apr 25 2003 Pixel <pixel@mandrakesoft.com> 0.7-5mdk
- add "BuildRequires: perl-devel"

* Thu Feb 13 2003 Pixel <pixel@mandrakesoft.com> 0.7-4mdk
- move to vendor_perl, fix %%files
- rebuild to have correct perl dependency

* Tue Jan 21 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.7-3mdk
- rebuild for latest emacs

* Wed Oct 17 2001 Pixel <pixel@mandrakesoft.com> 0.7-2mdk
- %%config(noreplace) the site-start.d/epl.el
- add the Source's url
- s/Copyright/License/

* Mon Feb 26 2001 Pixel <pixel@mandrakesoft.com> 0.7-1mdk
- initial spec

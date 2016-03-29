Summary: A tiling terminal emulator based on GTK+ 3
Name:terminix
Version: 0.55.1
Release: 1%{dist}
License: MPL
Group: Applications/Utilities

Source0: terminix-%{version}.tar.gz
URL: http://github.com/gnunn1/terminix

BuildRequires: gtk3-devel
BuildRequires: vte3-devel
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: dconf

Requires: gtk3
Requires: vte3
Requires: gsettings-desktop-schemas
Requires: dconf

Packager: Asif Ali Rizvan <fast.rizwaan@gmail.com>

%description
A tiling terminal emulator

%prep
exit 0

%build
exit 0

%install
unzip -x -d %buildroot %{SOURCE0} 

%files
%defattr(755,root,root)
%{_bindir}/terminix        
%{_datadir}/applications/com.gexperts.Terminix.desktop
%attr(644,root,root)  
%{_datadir}/terminix/schemes/tango.json  
%{_datadir}/terminix/schemes/solarized-light.json  
%{_datadir}/terminix/schemes/solarized-dark.json  
%{_datadir}/terminix/schemes/orchis.json  
%{_datadir}/terminix/schemes/linux.json  
%{_datadir}/terminix/resources/terminix.gresource  
%{_datadir}/glib-2.0/schemas/com.gexperts.Terminix.gschema.xml  
/usr/share/dbus-1/services/com.gexperts.Terminix.service
/usr/share/locale/de/LC_MESSAGES/terminix.mo
/usr/share/locale/en/LC_MESSAGES/terminix.mo
/usr/share/locale/fr/LC_MESSAGES/terminix.mo
/usr/share/locale/pt_BR/LC_MESSAGES/terminix.mo
/usr/share/locale/zh_CN/LC_MESSAGES/terminix.mo
/usr/share/locale/zh_TW/LC_MESSAGES/terminix.mo
/usr/share/nautilus-python/extensions/open-terminix.py
/usr/share/nautilus-python/extensions/open-terminix.pyc
/usr/share/nautilus-python/extensions/open-terminix.pyo
/usr/share/terminix/schemes/base16-twilight-dark.json
/usr/share/terminix/schemes/monokai.json

%post
/usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas/

%postun
/usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas/

%changelog
* Tue Mar 29 2016 Simone Del Prete <simone.delprete@bspa.it> 0.55.1-1
- i18n: Localize the about dialog. (ph.wolfer@gmail.com)
- i18n: German: Clarified search wrap around string (ph.wolfer@gmail.com)
- i18n: German translation for new strings (ph.wolfer@gmail.com)
- Various fixes related to shortcuts (gerald.b.nunn@gmail.com)
- Update version number to prepare for release (gerald.b.nunn@gmail.com)
- Add localization for ui files (gerald.b.nunn@gmail.com)
- Add support for reset dark theme property (gerald.b.nunn@gmail.com)
- Add initial support for GTKShortcutsWindow (gerald.b.nunn@gmail.com)
- Fix #185 (gerald.b.nunn@gmail.com)
- Fix issue with executing invalid file (gerald.b.nunn@gmail.com)
- Fix #184 (gerald.b.nunn@gmail.com)
- Add support for dynamic linking (gerald.b.nunn@gmail.com)
- Fix #158, keyboard shortcuts for resizing (gerald.b.nunn@gmail.com)
- Fix warning about regex null (gerald.b.nunn@gmail.com)
- Fix #180 (gerald.b.nunn@gmail.com)
- Enable Enter/Shift Enter key in search entry (gerald.b.nunn@gmail.com)
- Fix: po/pt_BR translating icon name in desktop file, resulting in missing
  icon (dsboger@gmail.com)
- Fix 1 border spacing issue with search entry (gerald.b.nunn@gmail.com)
- Fix search revealer border (gerald.b.nunn@gmail.com)
- Fix sidebar name alignment (gerald.b.nunn@gmail.com)
- Fix #165 (gerald.b.nunn@gmail.com)
- Change sidebar color to background (gerald.b.nunn@gmail.com)
- Fix sidebar transparent background (alex@alexwhitman.com)
- pt_BR updated - 100%% (fnogueira@gnome.org)
- Improve locating active AppWindow (gerald.b.nunn@gmail.com)
- Allow acl actions to be executed outside of terminix
  (gerald.b.nunn@gmail.com)
- Remove dbus flag (gerald.b.nunn@gmail.com)
- Fix #176 (gerald.b.nunn@gmail.com)
- Uninstall instructions (gerald.b.nunn@gmail.com)
- Don't create popover with model (gerald.b.nunn@gmail.com)
- Fix #169 (gerald.b.nunn@gmail.com)
- Add split buttons to popover menu (alex@alexwhitman.com)
- i18n: Typo in German translation (ph.wolfer@gmail.com)
- Shortcuts: Display "disabled" for disabled shortcuts in preferences.
  (ph.wolfer@gmail.com)
- Shortcuts: Do not save the localized disabled sting to config.
  (ph.wolfer@gmail.com)
- i18n: Updated German translation (ph.wolfer@gmail.com)
- i18n: Updated localized strings (ph.wolfer@gmail.com)
- i18n: Updated German translation (ph.wolfer@gmail.com)
- pt_BR ready to new shortcuts for next/prev session (fnogueira@gnome.org)
- Added Polish translation (psokol.l10n@gmail.com)
- added Russian translation (ashejn@gmail.com)
- [update-readme] added uninstallation instruction
  (pomba.magar@dragonlaw.com.hk)
- Add current session number to title (gerald.b.nunn@gmail.com)
- Display session name in sidebar (gerald.b.nunn@gmail.com)
- Uninstall script for #163 (gerald.b.nunn@gmail.com)
- Fix #164 (gerald.b.nunn@gmail.com)
- Fix #162 (gerald.b.nunn@gmail.com)
- Updated Korean Translation (sukso96100@gmail.com)
- Updated Korean Translation (sukso96100@gmail.com)
- Updated Korean Translation (sukso96100@gmail.com)
- Updated Korean Translation (sukso96100@gmail.com)
- Added Korean Translation (sukso96100@gmail.com)
- Fix #160 (gerald.b.nunn@gmail.com)
- Cleanup and centralize focusTerminal (gerald.b.nunn@gmail.com)
- Add directional terminal switching (alex@alexwhitman.com)
- Bump version number in prep for release (gerald.b.nunn@gmail.com)
- Increase opacity of drag highlight (gerald.b.nunn@gmail.com)
- Fix #153 (gerald.b.nunn@gmail.com)
- Improve notification counter positioning (gerald.b.nunn@gmail.com)
- Show notification count as badge on sidebar button (gerald.b.nunn@gmail.com)
- Fix #151 (gerald.b.nunn@gmail.com)
- Update title after Layout Options edited (gerald.b.nunn@gmail.com)
- Add new shortcuts for next/prev session (gerald.b.nunn@gmail.com)
- Fix #150 (gerald.b.nunn@gmail.com)
- Fix shortcut labels as per #138 (gerald.b.nunn@gmail.com)
- Debugging DND (gerald.b.nunn@gmail.com)
- Fix #142 (gerald.b.nunn@gmail.com)
- More improvement to #144 (gerald.b.nunn@gmail.com)
- Help with #144 by allowing search bar to shrink (gerald.b.nunn@gmail.com)
- Fix #148 (gerald.b.nunn@gmail.com)
- Fix #147 (gerald.b.nunn@gmail.com)
- Fix #149 (gerald.b.nunn@gmail.com)
- Fix #146 (gerald.b.nunn@gmail.com)
- pt_BR.po updated #144 (fnogueira@gnome.org)
- Changed resize=false, shrink=true for Paned sizing, #144
  (gerald.b.nunn@gmail.com)
- Add grabRemove when sidebar widget is unmapped, for #142
  (gerald.b.nunn@gmail.com)
- Test grab state before adding or removing it, for #142
  (gerald.b.nunn@gmail.com)
- Initial work for #143 (gerald.b.nunn@gmail.com)
- Fix #144 (gerald.b.nunn@gmail.com)
- Fix #141 (gerald.b.nunn@gmail.com)
- Fix #139 (gerald.b.nunn@gmail.com)
- l10n/zh_CN: keeping up with upstream (jeffbai@aosc.xyz)
- Fix #115 comment (gerald.b.nunn@gmail.com)
- Update localizations for numbering (gerald.b.nunn@gmail.com)
- Stage 3.20 fix for setting theme to Default (gerald.b.nunn@gmail.com)
- Add compile switch for ScrolledWindow testing (gerald.b.nunn@gmail.com)
- Update version number for release (gerald.b.nunn@gmail.com)
- Various code improvements (gerald.b.nunn@gmail.com)
- Update README.md (gnunn1@users.noreply.github.com)
- Remove notebook border for better look in Rawhide (gerald.b.nunn@gmail.com)
- Fix VTE State warnings on Rawhide (gerald.b.nunn@gmail.com)
- Fix issue with drag image on Rawhide (gerald.b.nunn@gmail.com)
- Fix small titlebars option in GTK 3.20 (gerald.b.nunn@gmail.com)
- Force master branch of GtkD to be used (gerald.b.nunn@gmail.com)
- Add new strings for localizing (gerald.b.nunn@gmail.com)
- Fix #134 (gerald.b.nunn@gmail.com)
- Fix #127, code improvements (gerald.b.nunn@gmail.com)
- Fix #128 (gerald.b.nunn@gmail.com)
- Fix #130 (gerald.b.nunn@gmail.com)
- Fix #131 (gerald.b.nunn@gmail.com)
- Fix #129 (gerald.b.nunn@gmail.com)
- Automatically wrap the info text in layout options dialog
  (ph.wolfer@gmail.com)
- Fix #33, side-effect of re-numbering terminals (gerald.b.nunn@gmail.com)
- Fix #122 (gerald.b.nunn@gmail.com)
- pt_BR.po - 101%% (fnogueira@gnome.org)
- i18n: Localize the "disabled" string for keyboard shortcuts
  (ph.wolfer@gmail.com)
- i18n: Updated German translation (ph.wolfer@gmail.com)
- i18n: Updated ranslation files (ph.wolfer@gmail.com)

* Thu Mar 03 2016 Simone Del Prete <simone.delprete@bspa.it> 0.51.0-2
- Look at dimming unfocused terminals (gerald.b.nunn@gmail.com)
- Fix #119 (gerald.b.nunn@gmail.com)

* Wed Mar 02 2016 Simone Del Prete <simone.delprete@bspa.it> 0.51.2-1
- new package built with tito

* Wed Mar 02 2016 Simone Del Prete <simone.delprete@bspa.it> 0.51.1-1
- new package built with tito


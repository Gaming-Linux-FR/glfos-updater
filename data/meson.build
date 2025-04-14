subdir('ui')
subdir('icons')

gnome = import('gnome')

gnome.compile_resources(
    'glfos-updater', 'glfos-updater.gresource.xml',
    gresource_bundle: true,
    dependencies: blueprints,
    install: true,
    install_dir: pkgdatadir
)

configure_file(
  input: 'org.glfos.updater.in',
  output: 'org.glfos.glfos-updater.policy',
  configuration: conf,
  install_dir: datadir / 'polkit-1' / 'actions'
)

configure_file(
  input: 'glfos-updater.desktop.in',
  output: 'glfos-updater.desktop',
  configuration: conf,
  install_dir: datadir / 'applications'
)
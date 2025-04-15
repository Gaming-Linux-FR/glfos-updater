blueprints = custom_target('blueprints',
  input: files(
    'window.blp',
    'welcome_dialog.blp',
    'welcome_dialog_welcome.blp',
    'welcome_dialog_stable.blp',
    'welcome_dialog_rolling.blp',
    'welcome_dialog_start.blp'
  ),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'],
)

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    //root_directory/templates/home.html
    //root_directory/templates/subdirectory/home.html
    './templates/**/*.html',

    //root_directory/app_name/templates/app_name/home.html
    //root_dirctory/another_app/templates/another_app/about.html
    './**/templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}


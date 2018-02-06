# Dsreports

Assemble html files to create static reports with [Hugo](https://gohugo.io/).

This was built to generate reports for the [Dataswim](https://github.com/synw/dataswim) library 
but can be used for other tasks. It is basically a boilerplate for Hugo.

It uses the [Bulma](http://bulma.io/) css framework

## Usage

To copy the Hugo base site to the current directory:

   ```
   python3 -m dsreports
   ```
   
Then go to `site/layouts/partials` and add html files.

Run `hugo server` to enable autoreload

Run `hugo` to build the static site: it will be located in `site/public`

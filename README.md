# ti.version

Python compile script to increment build versions for Appcelerator Titanium Mobile apps

## Usage

Just copy the `<ti.version>` folder into the `<plugins>` folder for your application.

Edit tiapp.xml, and add:
~~~
<plugins>
    <plugin version="0.1">ti.version</plugin>
</plugins>
~~~
That should create/update a file `<package.json>` in your `<Resources>` folder.

You can read the package.json file in app using:
~~~
var pjson = JSON.parse(Ti.Filesystem.getFile('./package.json').read());
Ti.API.info(pjson);
~~~
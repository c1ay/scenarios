### Introduction to shared libraries

The above is just a very simple example of a pipeline, however, in the enterprise, it is not so simple.

In enterprises, there are often very many projects, and some of them are so similar that only a few parts need to be modified when scheduling a Pipeline, so we can use **shared libraries** to reduce redundancy by sharing the pipeline.

\*The directory structure of **shared library** is as follows:

```bash
(root)
+- src # Groovy source files
| +- org
| +- foo
| +- Bar.groovy # for org.foo.Bar class
+- vars
| +- foo.groovy # for global 'foo' variable
| +- foo.txt # help for 'foo' variable
+- resources # resource files (external libraries only)
| +- org
| +- foo
| +- bar.json # static helper data for org.foo.Bar
Bar

where:

- src directory resembles the standard Java source directory structure. This directory is added to the class path when the pipeline is executed.
- The vars directory holds scripts for global variables that can be accessed from the pipeline. The basename of each `*.groovy` file should be a `Groovy (~ Java)` identifier, usually camelCased. Matching `*.txt`, if present, may contain documentation, formatted from the processing by the system's configuration markup (so it may be HTML, Markdown, etc., although the txt extension is required).
  The Groovy source files in these directories are the same as the "CPS transformation" in the scripting pipeline.
- The resources directory allows loading relevant non-Groovy files from external libraries using the libraryResource step. Currently, the internal library does not support this feature.
- The other directories in the root directory are reserved for future enhancements.
```

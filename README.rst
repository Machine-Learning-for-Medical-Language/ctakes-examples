Example physician notes
=======================

This package contains over two thousand sample physician notes,
for testing natural language processing.

There is no personal health information (PHI) in this repository.
All examples are either automatically generated (synthetic) or manually created for realism (curated).


Usage
=====

There are two expected ways to use these examples: indiscriminately and specifically.

That is, you might either just want a large corpus of text to iterate over,
or you might be looking to test a specific example in mind for regression testing.

We have APIs for both uses.

Listing All Example Files
-------------------------

If you just want to drink from the firehose and iterate over all examples, here's an easy way to do that.

.. code-block:: python3

   import ctakes_examples

   curated_examples = ctakes_examples.list_curated()
   assert curated_examples[0] == '/usr/lib/python3/ctakes_examples/resources/curated/1-year-old-exam-hp.txt'

   synthetic_examples = ctakes_examples.list_synthetic()
   assert curated_examples[0] == '/usr/lib/python3/ctakes_examples/resources/synthetic/13d7f763-ca16-76f5-ceae-6317aea0c44b.txt'

Reading Specific Examples
-------------------------

On the other hand, if you are testing for a specific interaction or regression,
it's also easy to grab a well-known single example note:

.. code-block:: python3

   import ctakes_examples

   curated = ctakes_examples.read_curated('wound-check-status-post-apr')
   assert curated.startswith('\n\nHISTORY OF PRESENT ILLNESS: Ms. Connor is a 50-year-old female')

   synthetic = ctakes_examples.read_synthetic('3bf82678-8a31-e0ba-910a-a12ccceb9c4e')
   assert synthetic.startswith('\n2021-01-26\n\n# Chief Complaint')

Consistency Promise
===================

To the best of our ability, we will not change the names or contents of existing examples.
If we must do so, it will be considered a breaking change and we'll bump the major version of this package.

New files might be added during any update though.

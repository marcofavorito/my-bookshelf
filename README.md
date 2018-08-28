# my-bookshelf
Collection of books, papers, list of papers, blog or blog posts, articles that I've read/I'm going to read/I would remember that they exist/It is unlikely that I'll read/I'll never read.

The list of items is stored in [`bookshelf.txt`](./bookshelf.txt) in the following format:

    item_name1 \t link1 \t tag1 \t tag2 \t ...
    item_name2 \t link2 \t tag1 \t tag2 \t ...

Please go to [marcofavorito.github.io/my-bookshelf/](https://marcofavorito.github.io/my-bookshelf/) for the interactive version.

It's more a proof of concept rather than an established solution. It might change in the future.

## Why?
I always wanted to take care of a list of documents (books, papers, etc.) for my studies, both for the university, insights and other personal interests.

I tried to _download_ and store these files, or a list of them, on local file system and backed up whenever needed. But it seemed to me a dispersive work, and in this way you cannot store nice websites, web articles or blog posts, that quite often are very valuable.

I tried to keep up a list of _bookmarks_ on my favourite web browser, but... I ended up with thousands of bookmarked pages, organized in no structured and consistent way.

I thought about a self-hosted website, but I have not so much time to set up it.

... And this repository is my last (naive) solution. It lies somehow in the middle of the previous solutions:
- No need to download everything, just keep the reference with the link provided;
- No need to bookmark everything, and the links are automatically organized by leveraging the tag mechanism.
- No need to self-host a website, just use the nice GitHub Pages.

Moreover, anyone can see this list (and contribute to it!), so maybe someone find it useful.

It can be improved a lot, e.g:
- the list could easily contain duplicates or inconsistencies
- no detailed info for each item
- possibility of dead links
- arbitrary tag selection
- ...

A more structured solution would be to use a database, but too much time to insert an item manually (title, authors, date, etc.)... Maybe one could build a program that from the provided link it infers all the information you want... But that's another story.


## What?
You'll find many textbook, papers, articles, blog posts, readings and similar in the field of Computer Science and related. You might find also documents about topics like Math, Physics and other scientific fields, as well as non-scientific ones like economics and philosophy.

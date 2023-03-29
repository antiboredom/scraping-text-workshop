Web scraping involves downloading and then parsing web pages, which means you need to have some basic understanding of how HTML and CSS work.

## HTML

HTML is made up of elements. Elements are made of tags.

Most elements have an opening tag, some content, and then a closing tag.

```html
<tagname>some content goes here</tagname>
```

Here's a paragraph tag:

```html
<p>I'm a paragraph</p>
```

Different tags are used for different types of content:

- `p`: paragraph of text
- `a`: a link
- `ul` : unordered (bulleted) list
- `li`: a list item
- `strong`: important text
- `h1`: A large headline
- `h2`: A smaller headline
- `div`: a widely used tag to signify a division or section of content

### Attributes

Elements can also have **attributes**. These are key/value pairs that declare extra information about the tag. An attribute looks like this:

```html
<tagname attributename="value">content</tagname>
```

Some attributes can be applied to any tag. The two most important ones (for our purposes) are `id` and `class`.

The `id` attribute gives a **unique** identifier to a tag. There can only be **one** tag with any given `id`.

```html
<p id="the-most-important-paragraph">This is the most important paragraph.</p>
```

The `class` attribute indicates a user-defined category for an element. Many elements (including different types of tags) can share the same class name.

```html
<p class="sort-of-important">I'm a sort of important paragraph</p>

<p class="sort-of-important">I'm also a sort of important paragraph</p>

<div class="sort-of-important">I'm another a sort of important thing</div>
```

Some attributes are specific to certain tags.

The `a` tag, for example, requires an `href` attribute that indicates where the browser should navigate to when someone clicks on it.

```html
<a href="http://whitehouse.gov">don't click here</a>
```

Some elements DON'T have a closing tag. The image tag, for example, doesn't have a closing tag but requires the `src` attribute to be set:

```html
<img src="lolcapitalism.jpg" />
```

### A Barebones Webpage

All HTML documents contain the following tags:

- `html`: Surrounds the entire document
- `head`: A tag that doesn't render to the page but contains important links to style sheets and the title tag
- `title`: The title of the page
- `body`: Surrounds the body of the page

HTML elements are nested within other elements.

For example, here's a complete HTML document:

```html
<html>
  <head>
    <title>My Cool Website</title>
  </head>
  <body>
    <div>
      <h1>A Communisty Manifesto</h1>

      <p>Many <strong>spectres</strong> are haunting Europe. Here are some of them:</p>

      <ul>
        <li>The first spectre</li>
        <li>The second spectre</li>
        <li>The third spectre</li>
      </ul>

      <img src="so-many-spectres.jpg" />

      <p>Keep reading to find out all of the spectres currently haunting Europe!</p>
    </div>
  </body>
</html>
```

Note the indentations. These are completely optional (the machine doesn't care if you indent or not), but it's good practice to always indent elements inside of other elements because it helps show the structure of the document.

##CSS

CSS stands for "cascading stylesheet".

CSS determines the look of a website, both positioning elements on the screen and giving them visual attributes like color, or font size.

Many of the particulars of CSS styling are irrelevant for this guide. What matters for us is the syntax that determines how styles are applied, because it provides a handy system for isolating and extracting particular elements from an HTML document.

A css style is made of a `selector` followed by `rules`. We don't care about the rules, just the selector. Here is a bit of fake CSS:

```css
selector {
  /* the bit before the squiqqly is called the "selector" */
  rule: some rule here; /* these are rules, we don't care about them */
  another-rule: more rules; /* more rules */
}
```

The selector determines what gets styled. Selectors can be used to target all instances of a particular tag, elements with particular classes or ids, and other more complex rules.

You can target every instance of a tag by referencing the name of the tag:

```css
p {
  color: red;
}
```

You can also give style to tags that have particular ids or classes.

Select classes by preceding the class name with a period `.` character. For example, select all tags with the "proletariat" class:

```css
.proletariate {
  background-color: red;
}
```

Select ids by preceding the id name with a hashtag `#` character.

```css
#the-manifesto {
  border: 10px solid orange;
}
```

You can also select elements that are **_inside_** other elements, by first writing the parent element, then a space, then the child element.

For example, this selects `a` tags that are INSIDE `p` tags:

```css
p a {
  background-color: black;
}
```

You can also do this with classes and ids. This selects `span` tags found inside elements with the `author` class.

```css
.author span {
  color: pink;
}
```

You can use the comma to get multiple selectors. The following grabs h1 tags and h2 tags:

```css
h1,
h2 {
  color: orange;
}
```

Here's a [full list of css selectors](https://www.w3schools.com/cssref/css_selectors.asp).

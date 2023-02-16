# 0x01. AirBnB clone - Web static

## Tasks

### 0. Inline styling
Write an HTML page that displays a header and a footer.

Layout:

<ul>
<li>body:<ul><li>no margin</li><li>no padding</li></ul></li>
<li>Header:<ul><li>color #FF0000 (red)</li><li>height: 70px</li><li>width: 100%</li></ul></li>
<li>Footer:<ul><li>color #00FF00 (green)</li><li>height: 60px</li><li>width: 100%</li><li>text Best School center vertically and horizontally</li><li>always at the bottom at the page</li></ul>
</ul>

Requirements:
<ul>
<li>You must use the header and footer tags</li>
<li>You are not allowed to import any files</li>
<li>You are not allowed to use the style tag in the head tag</li>
<li>Use inline styling for all your tags</li>
</ul>

![hbnb](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/98f4ac1b0644512ce7ae91a9e8e61e8fe174911d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230216T143453Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5765e210b4c27836d19b0b48ee09a7105624d1031478310dc7a9bbe7c805534d)


### 1. Head styling
Write an HTML page that displays a header and a footer by using the style tag in the head tag (same as 0-index.html)

Requirements:
<ul>
<li>You must use the header and footer tags</li>
<li>You are not allowed to import any files</li>
<li>No inline styling</li>
<li>You must use the style tag in the head tag</li>
</ul>


### 2. CSS files
Write an HTML page that displays a header and a footer by using CSS files (same as 1-index.html)

Requirements:
<ul>
<li>You must use the header and footer tags</li>
<li>No inline styling</li>
<li>You must have 3 CSS files: <ul><li>styles/2-common.css: for global style (i.e. the body style)</li><li>styles/2-header.css: for header style</li><li>styles/2-footer.css: for footer style</li>
</ul>

The layout must be exactly the same as 1-index.html


### 3. Zoning done!
Write an HTML page that displays a header and footer by using CSS files (same as 2-index.html)

Layout:
<ul>
<li>Common: <ul><li>no margin</li><li>no padding</li><li>font color: #484848</li><li>font size: 14px</li><li>font family: Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;</li><li><a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon.png">icon</a> in the browser tab</li></ul></li>
<li>Header: <ul><li>color: white</li><li>height: 70px</li><li>width: 100%</li><li>border bottom 1px #CCCCCC</li><li><a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/logo.png">logo</a> align on left and center vertically (20px space at the left)</li></ul></li>
<li>Footer: <ul><li>color white</li><li>height: 60px</li><li>width: 100%</li><li>border top 1px #CCCCCC</li><li>text Best School center vertically and horizontally</li><li>always at the bottom at the page</li></ul></li>
</ul>

Requirements:
<ul>
<li>No inline style</li>
<li>You are not allowed to use the img tag</li>
<li>You are not allowed to use the style tag in the head tag</li>
<li>All images must be stored in the images folder</li>
<li>You must have 3 CSS files: <ul><li>styles/3-common.css: for the global style (i.e body style)</li><li>styles/3-header.css: for the header style</li><li>styles/3-footer.css: for the footer style</li></ul>
</ul>

![hbnb](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/2be1eda05a0d9097c210f2d3482a59aa858c5711.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230216T143453Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5c8f287c7b01778bb33f777cc21eab6852748f544de967b284719cfb844f2f1c)


### 4. Search!
Write an HTML page that displays a header, footer and a filters box with a search button.

Layout: (based on 3-index.html)
<ul>
<li>Container: <ul><li>between header and footer tags, add a div: <ul><li>classname: container</li><li>max width 1000px</li><li>margin top and bottom 30px - it should be 30px under the bottom of the header (screenshot)</li><li>center horizontally</li></ul></li></ul></li>
<li>Filter section: <ul><li>tag section</li><li>classname filters</li><li>inside the .container</li><li>color white</li><li>height: 70px</li><li>width: 100% of the container</li><li>border 1px #DDDDDD with radius 4px</li></ul></li>
<li>Button search: <ul><li>tag button</li><li>text Search</li><li>font size: 18px</li><li>inside the section filters</li><li>background color #FF5A5F</li><li>text color #FFFFFF</li><li>height: 48px</li><li>width: 20% of the section filters</li><li>no borders</li><li>border radius: 4px</li><li>center vertically and at 30px of the right border</li><li>change opacity to 90% when the mouse is on the button</li></ul></li>
</ul>

Requirements:
<ul>
<li>You must use: header, footer, section, button tags</li>
<li>No inline style</li>
<li>You are not allowed to use the img tag</li>
<li>You are not allowed to use the style tag in the head tag</li>
<li>All images must be stored in the images folder</li>
<li>You must have 4 CSS files: <ul><li>styles/4-common.css: for the global style (body and .container styles)</li><li>styles/3-header.css: for the header style</li><li>styles/3-footer.css: for the footer style</li><li>styles/4-filters.css: for the filters style</li></ul></li>
<li>4-index.html won’t be W3C valid, don’t worry, it’s temporary</li>
</ul>

![hbnb](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/f959154b0cdf1cdf71ddef04e3787ef28462793e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230216T143453Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bf57db951323015338ec824f886b18efa37916ff50e41fe33384e67be5694df9)


### 5. More filters
Write an HTML page that displays a header, footer and a filters box.

Layout: (based on 4-index.html)
<ul>
<li>Locations and Amenities filters: <ul><li>tag: div</li><li>classname: locations for location tag and amenities for the other</li><li>inside the section filters (same level as the button Search)</li><li>height: 100% of the section filters</li><li>width: 25% of the section filters</li><li>border right #DDDDDD 1px only for the first left filter</li><li>contains a title: <ul><li>tag: h3</li><li>font weight: 600</li><li>text States or Amenities</li></ul></li><li>contains a subtitle: <ul><li>tag: h4</li><li>font weight: 400</li><li>font size: 14px</li><li>text with fake contents</li></ul></li></ul></li>
</ul>

Requirements:
<ul>
<li>You must use: header, footer, section, button, h3, h4 tags</li>
<li>No inline style</li>
<li>You are not allowed to use the img tag</li>
<li>You are not allowed to use the style tag in the head tag</li>
<li>All images must be stored in the images folder</li>
<li>You must have 4 CSS files: <ul><li>styles/4-common.css: for the global style (body and .container styles)</li><li>styles/3-header.css: for the header style</li><li>styles/3-footer.css: for the footer style</li><li>styles/5-filters.css: for the filters style</li></ul></li>
</ul>

![hbnb](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/85bfa50b96c2985723daa75b5e22f75ef16e2b2e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230216T143453Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=512a91b43ad55cee59c30cc64bae9e9a76423aedf0778cad4e13a1ac73eae166)


### 6. It's (h)over
Write an HTML page that displays a header, footer and a filters box with dropdown.

Layout: (based on 5-index.html)
<ul>
<li>Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter div: <ul><li>tag ul</li><li>classname popover</li><li>text should be fake now</li><li>inside each div</li><li>not displayed by default</li><li>color #FAFAFA</li><li>width same as the div filter</li><li>border #DDDDDD 1px with border radius 4px</li><li>no list display</li><li>Location filter has 2 levels of ul/li: <ul><li>state -> cities</li><li>state name must be display in a h2 tag (font size 16px)</li></ul></li></ul></li>
</ul>

Requirements:
<ul>
<li>You must use: header, footer, section, button, h3, h4, ul, li tags</li>
<li>No inline style</li>
<li>You are not allowed to use the img tag</li>
<li>You are not allowed to use the style tag in the head tag</li>
<li>All images must be stored in the images folder</li>
<li>You must have 4 CSS files: <ul><li>styles/4-common.css: for the global style (body and .container styles)</li><li>styles/3-header.css: for the header style</li><li>styles/3-footer.css: for the footer style</li><li>styles/6-filters.css: for the filters style</li></ul></li>
</ul>

![hbnb](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/6262f13624dca23ca19db505c44f88faddb82ebb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230216T143453Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e19a357077d2b72a420f95fbd5e2f571ad43bc9053061313a3100962fbb5af8b)

![hbnb](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/6e6bdfa13fa88a5f439d9e2b1dade826dd95529b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230216T143453Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c9812d49279f31ed22d7174812b8fd88397798ce0f95ae5d0a4e52d2319f31b4)


### 7. Display results
Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on 6-index.html)
<ul>
<li>Add Places section: <ul><li>tag: section</li><li>classname: places</li><li>same level as the filters section, inside .container</li><li>contains a title: <ul><li>tag: h1</li><li>text: Places</li><li>align in the top left</li><li>font size: 30px</li></ul></li><li>contains multiple “Places” as listing (horizontal or vertical) describe by: <ul<li>tag: article</li><li>width: 390px</li><li>padding and margin 20px</li><li>border #FF5A5F 1px with radius 4px</li><li>contains the place name: <ul><li>tag: h2</li><li>font size: 30px</li><li>center horizontally</li></ul></li></ul></li></ul></li>
</ul>

Requirements:
<ul>
<li>You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags</li>
<li>No inline style</li>
<li>You are not allowed to use the img tag</li>
<li>You are not allowed to use the style tag in the head tag</li>
<li>All images must be stored in the images folder</li>
<li>You must have 5 CSS files: <ul><li>styles/4-common.css: for the global style (i.e. body and .container styles)</li><li>styles/3-header.css: for the header style</li><li>styles/3-footer.css: for footer style</li><li>styles/6-filters.css: for the filters style</li><li>styles/7-places.css: for the places style</li></ul></li>
</ul>

![hbnb](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/bca4d17fbe21a58b66a9d5d6b85df4801d147dd0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230216T143453Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7a840203e56055e80b11e91da26fbf8c9b81e41c835e514d51ea7bfa4546e50c)


### 8. More details
Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.

Layout: (based on 7-index.html)

Add more information to a Place article:
<ul>
<li>Price by night: <ul><li>tag: div</li><li>classname: price_by_night</li><li>same level as the place name</li><li>font color: #FF5A5F</li><li>border: #FF5A5F 4px rounded</li><li>min width: 60px</li><li>height: 60px</li><li>font size: 30px</li><li>align: the top right (with space)</li></ul></li>
<li>Information section: <ul><li>tag: div</li><li>classname: information</li><li>height: 80px</li><li>border: top and bottom #DDDDDD 1px</li><li>contains (align vertically): <ul><li>Number of guests: <ul><li>tag: div</li><li>classname: max_guest</li><li>width: 100px</li><li>fake text</li><li><a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_group.png">icon</a></li></ul></li><li>Number of bedrooms: <ul><li>tag: div</li><li>classname: number_rooms</li><li>width: 100px</li><li>fake text</li><li><a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_bed.png">icon</a></li></ul></li><li>Number of bathrooms: <ul><li>tag: div</li><li>classname: number_bathrooms</li><li>width: 100px</li><li>fake text</li><li><a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_bath.png">icon</a></li></ul></li></ul></li></ul></li>
<li>User section: <ul><li>tag: div</li><li>classname: user</li><li>text Owner: <fake text></li><li>Owner text should be in bold</li></ul></li>
<li>Description section: <ul><li>tag: div</li><li>classname: description</li></ul></li>
</ul>

Requirements:
<ul>
<li>You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags</li>
<li>No inline style</li>
<li>You are not allowed to use the img tag</li>
<li>You are not allowed to use the style tag in the head tag</li>
<li>All images must be stored in the images folder</li>
<li>You must have 5 CSS files: <ul><li>styles/4-common.css: for the global style (i.e. body and .container styles)</li><li>styles/3-header.css: for the header style</li><li>styles/3-footer.css: for the footer style</li><li>styles/6-filters.css: for the filters style</li><li>styles/8-places.css: for the places style</ul></li>
</ul>

![hbnb](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/f4b2d4ef94bd3a2e7e1ddefa81236595686d270e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230216T143453Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=18ea4e96f975b5aca0df65021d6ef152e21d7a6b1b875da4baf109b1de393d99)


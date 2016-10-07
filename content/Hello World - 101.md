Title: Hello World - 101
Date: 2016-05-07 5:30 PM
Modified: 2016-07-02 11:00 PM
Category: Github
Tags: pelican, publishing, markdown, github, settings
Summary: Setting up my techblog using [pelican](https://docs.getpelican.com/en/) 


# Hi Everyone!

For so long I have been thinking of setting up a proper techblog for myself. One that would give the feel of being a real technical corner of amusement - a geeky touch. A sneak peek into the life of an aspiring product designer presented from a learner's perspective.

I love creative writing and for that I have been blogging on wordpress for over two years now. You can find my blog [here](https://thevindicatedaxiom.wordpress.com). I also created a [**techblog**](https://thevindicatedaxiom.wordpress.com/category/techblog) category there but I wasn't fully satisfied with this mocktail of two entirely diverse interests. Science with philosophy is indeed a dangerous combination. 

I love learning new things that spans [wide range of things](https://about.me/chandan_sinha) but mostly its all about exciting technology. Latest or obselete, innovation has always fascinated me and when I experience it first hand, my joy knows no bound. The tech-enthusiast inside me always wanted to ramble its learning endeavour - for the sake of documentation and for helping the passionately curious beings like me out there.

So I looked into the alternatives and found this awesome static site generator ['Pelican'](http://getpelican.com/) powered by python. It allows me to write down things in Markdown, which I make most of my notes in anyway.

## Creating a separate github account

I already have one [website](https://mechanicalcoder.github.io) running from my [main github account](https://github.com/mechanicalcoder). Earlier I thought I could serve my techblog from the same repository by creating a sub-folder but ghpages couldn't generate the webpage. Github is quite smart to know that the website files lie within the <i>output</i> folder.

So I had to make a [separate Github account](https://github.com/mechandansinha) where I could push just the <i>output</i> folder in the repository named <i> username.github.io </i>.

Apart from the generated output, you can also find the entire blog repository on [my Github account](https://github.com/mechandansinha/Techblog.git).

## Setting up

I won't mention all the things that I did to setup my blog as it has already been extensively written in many blog posts. Refer to the resources below. After I was through with [quickstart](https://docs.getpelican.com/en/3.6.3/quickstart.html), I initialized git inside my <i>output</i> folder. Also I added my github repository as 'remote'.

```sh
$ cd output
$ git init
$ git remote add origin https://github.com/username.username.github.io.git
```
## Resources

These two blog posts were extremely useful throughout the set-up procedure. Right from the basics, they have also mentioned the customizations you could do if you want to play around. 

- http://mathamy.com/migrating-to-github-pages-using-pelican.html
- http://thesoftjaguar.com/posts/2013/04/06/pelican-static-blog/

I would definitely suggest reading the [pelican docs](http://docs.getpelican.com/) to understand different features. Also if you have an existing blog on other platforms like wordpress, you can import the contents directly as mentioned in the docs.

## Theme

I'm using **Flex** in my blog. I went through almost 40 themes to finally settle with this one. To understand how can I utilize the various customizations this themes offer, [Flex wiki](https://github.com/alexandrevicenzi/Flex/wiki) page was extremely useful. They have shown it with examples as well. 

There's just one thing to be taken care of. Whatever editing is to be done, we do it in <i>pelicanconf.py</i> file. All the variables would be defined there.

## Disqus Integration

Disqus provides a sophisticated platform for discussion through comments. Disqus integration was really easy as I just had to create one disqus account and follow their procedures to create a channel for my website. 

Then you just have to include your disqus sitename (this can't be changed afterwards) under DISQUS_SITENAME in the configuration file.

## Let's get started

I am really excited to finally have a separate techblog. Hope you would find this space interesting. Stay tuned and keep reading about my journey through technical extravaganza of **_making things that matter_**.

If you're a complete beginner & interested in knowing what exactly did I write in markdown for this post, here is the gist for you. Enjoy!

<script src="https://gist.github.com/MechanicalCoder/576c2f2e33f6abd758d97dbf7ae35fa9.js"></script>

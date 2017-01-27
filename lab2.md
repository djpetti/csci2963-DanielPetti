#Having a License

U.S. copyright law is such that, if your software contains no explicit liscense,
then it is assumed to be "all rights reserved". This means that, even if you
post it on GitHub, technically the software is not free. Because of this, you
should always add an OSI-approved license to software that is intended to be
free.

#Not Using Projects Without a License

If you use a project without a license, even if it is available for free, you
are essential forgoing legal protection of your freedom to use the software as
you wish. This means that, under certain circumstances, you could face a
lawsuit for your actions. In order to avoid this, make sure that the
software that you use has a license that legally protects the actions you want
to take with it.

#The Rise and Fall of Gopher

In retrospect, the claim that Gopher failed because it did not follow an open
model seems pretty clear, especially after reading "The Cathedral and the
Bazaar." Clearly, WWW moved towards the latter model as Gopher stuck with the
former, which effectively reduced the number of developers seriously involved
with Gopher compared to WWW, and contributed to its demise. In practice, most
likely there were a wide range of factors that caused this outcome, but the one
outlined in this article seems quite plausible.

#Justifying the Android Kernel License

This is actually trivial, because the Android Kernel is basically Linux. Since
Linux itself is GPL liscensed, then, clearly, Android is legally obligated to
use the same license.

#Example: Choosing a License

Let's consider a situation that it actually relatively common these days:

Imagine that I work for a company that builds hardware which requires custom
software. Perhaps I want to make this software open source, if, for instance, my
company stands to benefit from a lot of users using my software on other
people's platforms. As an example of this, think of something like Android, in
which Google has clear motivations to get its OS running on as many devices as
possible, even if they only physically manufacture a small fraction of them.

In this case, I might want to choose a permissive license, such as the MIT
license. This type of license poses the least hassle to people who want to use
my software, so, naturally, it seems logical that, if I want to build a large
user base, I should use that license.

I could also make an argument for using a copyleft license like GPL, however,
especially if I were feeling vindictive and wanted to ensure that other
companies could not simply rip off my code, package it into a proprietary
system, and sell it.

#Which license is better?

*Common Good:* GPL wins on this one. By expressly requiring that all derivative
works be distributed with the same license, the GPL compels users to share their
modifications and grow the community.

*For Developers:* LGPL makes life easier for developers by explicitly not
requiring works that only use the software as a dynamically-linked library to
bear the LGPL license. This is extremely useful for developers, because it
allows them to make use of a large suite of free, standard libraries, even when
they are working on a proprietary product.

*For Companies:* The Apache license is nice for companies, because they can
basically do whatever they want. They can modify the software and use it
directly in a proprietary product. Furthermore, they can make patent claims on
these modifications.

#Project for this Course

I will be working on my RCOS project,
[GroBot](https://github.com/djpetti/grobot). Currently, GroBot uses the MIT
license, which I just chose because, frankly, I didn't care how people used it.
I am considering switching to GPL, however, mainly because this is software that
goes with a specific hardware product, and I don't want people who make a
competing hardware product to simply rip off my code and sell it as part of a
proprietary system. To me, this does not seem fair, both to me, to their users,
and to my users.

#RCOS License Survey

| Website | License Present? | License |
| ------- | ---------------- | ------- |
| [Solum](http://git.polaritech.com/Solum/Solum/tree/master) | Yes | MIT |
| [CarLogic API](https://github.com/burtonwilliamt/carlogicapi) | Yes | Apache |
| [CuBl](https://github.com/mcaniw/CuBl) | Yes | MIT |
| [CodeCombat](https://github.com/codecombat/codecombat) | Yes | MIT |
| [Knowledge API](https://github.com/rellink/knowledge-api) | Yes | MIT |

![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png) This work is licensed under a http://creativecommons.org/licenses/by/4.0/ Creative Commons Attribution 4.0 International License.

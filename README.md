# twitch_sgqlc
> A conversion of [Twitch's GraphQL schema](https://github.com/SuperSonicHub1/twitch-graphql-api) to a [sgqlc](https://github.com/profusion/sgqlc) Schema.

## Usage
> To be created...

## Roadmap
* Document basic usage
* Create tests

## NOTE!
When generating the schema, make sure to change the `Time` variable from `sgqlc.types.datetime.Time` to `sgqlc.types.datetime.DateTime`. **IF YOU DON'T DO THIS, THE LIBRARY WILL BREAK!**

## License
This entire repository is licensed under the *I Solemny Swear That I Am Up To No Good Public License*, a modification of the [WTFPL](http://www.wtfpl.net/) by [d0nk](https://github.com/d0nk) for the release of [parler-tricks](https://github.com/d0nk/parler-tricks), effectively releasing this body of work into the public domain.

import os
import argparse
from pyencourage import pyencourage


def create_argparser():
    parser = argparse.ArgumentParser(
        description='One line encouragements for programmers (encouragement as a service)'
    )

    parser.add_argument(
        '-c', '--category',
        dest='category',
        choices=['neutral', 'all', ],
        default='neutral',
        help='Encouragement category.'
    )

    parser.add_argument(
        '-l', '--language',
        dest='language',
        choices=['en'],
        default='en',
        help='Encouragement language.'
    )

    return parser


def main():
    parser = create_argparser()

    try:
        args = parser.parse_args()
    except argparse.ArgumentError as exc:
        print('Error parsing arguments.')
        parser.error(str(exc.message))
        exit(-1)

    try:
        encouragement = pyencourage.get_encouragement(language=args.language, category=args.category)
    except pyencourage.LanguageNotFoundError:
        print(f'No such language {args.language}')
        exit(-1)
    except pyencourage.CategoryNotFoundError:
        print(f'No such category {args.category}')
        exit(-1)

    print(encouragement)

if __name__ == '__main__':
    main()

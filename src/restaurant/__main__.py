#!/usr/bin/env python3

import click
from restaurant.restaurants import Diner, CoffeeShop

@click.command("coffeeshop")
def coffeeshop():
    java = CoffeeShop("Java")
    java.take_order()
    click.echo("\n")
    java.deliver_orders()

@click.command("diner")
def diner():
    owlcafe = Diner("The Owl Café")
    owlcafe.take_order()
    click.echo("\n")
    owlcafe.deliver_orders()

@click.group()
@click.pass_context
def main(ctx):
    pass

main.add_command(coffeeshop)
main.add_command(diner)



if __name__ == '__main__':
    main()

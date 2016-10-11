#!/usr/bin/env python

# Import
import sys
import os
import socket

# Set input file path with domains separated by lines
domains_input = raw_input("Enter input domains file (lookup/domains-input.txt): ")

# Set output file path with domains separated by lines
domains_output = raw_input("Enter input domains file (lookup/domains-output.txt): ")

# Define the default path for input domains file
if domains_input == "":
    domains_input = os.getcwd() + "/lookup/domains-input.txt"

# Define the default path for output domains file
if domains_output == "":
    domains_output = os.getcwd() + "/lookup/domains-output.txt"

# Create output domains file
open(domains_output, 'w').close()

try:
    # Try to open input domains file
    with open(domains_input, "r") as domains:
        # Fetch domains
        for domain in domains:
            try:
                # Try to resolve IP address
                line = domain.replace("\n", "") + " - " + socket.getaddrinfo(domain.replace("\n", ""), 80)[0][4][0]
            except Exception, error:
                # Output exception
                line = domain.replace("\n", "") + " - " + str(error)

            # Print line
            print line

            # Write line to output domains file
            with open(domains_output, "a") as file:
                file.write(line + "\n")

except Exception, error:
    # Output exception
    print "Error: " + error

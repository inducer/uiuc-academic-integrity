#! /bin/bash

exec ./hearing-to-events \
	--grist-root-url https://scicomp-grist.cs.illinois.edu \
	--grist-doc-id s7VzXiAHXbwgivucYprb6z \
	--grist-api-key ~/.grist-uiuc-api-key \
	"$@"

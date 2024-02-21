#! /bin/bash

exec ../update-outlook \
	--grist-root-url https://scicomp-grist.cs.illinois.edu \
	--grist-doc-id s7VzXiAHXbwgivucYprb6z \
	--grist-api-key ~/.grist-uiuc-api-key \
	--calendar-id AAMkADY3YjZmODE0LWEyMjgtNDUxZC1hNDkwLWZiMzg0YTIzYzFkMgBGAAAAAAAqtqQ1k44CSLzWsTHAiXTyBwAZE5V6g2ghS5C2mPF0FFfSAAAA7SAOAADYC-6OOu3iSo_9km74hr7sAAUcemO7AAA= \
	"$@"

import re


URL_regex = re.compile(
    r"""
    (?P<scheme>[a-z][a-z0-9]*(?:\+[a-z][a-z0-9]*)?://?)
    (?P<netloc>
        (?P<auth>
            (?P<username>[a-zA-Z0-9-._~!$&'()*+,;=]+)
            (?::(?P<password>[a-zA-Z0-9-._~!$&'()*+,;=]+))?@
        )?
        (?P<host>
            (?P<ipv4>(?:(?:25[0-5]|(?:2[0-4]|1\d|[1-9]|)\d)\.?\b){4}) |
            (?P<ipv6>\[(?:[a-fA-F0-9]{0,4}:){1,7}[a-fA-F0-9]{0,4}\]) |
            (?P<domain>(?:[-a-zA-Z0-9_]+\.){1,3}[-a-zA-Z0-9_]+) |
            (?P<hostname>[-a-zA-Z0-9_]+)
        )
        (?::(?P<port>\d+))?
    )
    (?P<path>(/[-a-zA-Z0-9_.]+)+/?)?
    (?:;(?P<params>[^?]*))?
    (?:\?(?P<query>[-a-zA-Z0-9_=&]+))?
    (?:\#(?P<fragment>[-a-zA-Z0-9_]+))?
    """,
    re.VERBOSE,
)


WINDOWS_PATH_REGEX_PYTEST = re.compile(
    r"""
    (?P<path>(?:[^\\/:*?\"<>|\r\n\s]+\\)*.*\.py)(?P<lineno>:\d+:) |
    rootdir:\ (?P<rootdir>.*)
    """,
    re.VERBOSE,
)

UNIX_PATH_REGEX_PYTEST = re.compile(
    r"""
    (?P<path>/?(?:[^/\s]+/)*.*\.py)(?P<lineno>:\d+:) |
    rootdir:\ (?P<rootdir>.*)
    """,
    re.VERBOSE,
)

PLANT_UML_SEQUENCE = re.compile(
    (
        r"""
                ^
                (?P<actor>.*)\s+<?-+>?\s+(?P<receiver>.*):\s+
                (?P<method>GET|PUT|POST|DELETE|OPTIONS|HEAD|PATCH|TRACE)\s+
                (?P<path>
                    (?P<segment>(/[-a-zA-Z0-9_.{}\[\]]+)+/?)
                    (?:;(?P<params>[^?]*))?
                    (?:\?(?P<query>[-a-zA-Z0-9_=&]+))?
                    (?:\#(?P<fragment>[-a-zA-Z0-9_]+))?
                )
                .*
                \n
                (?P=receiver)\s+<?-+>?\s+(?P=actor):\s+(?P<response>.*)$
                """
    ),
    re.MULTILINE | re.VERBOSE,
)

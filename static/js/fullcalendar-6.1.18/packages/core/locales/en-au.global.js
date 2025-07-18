/*!
FullCalendar Core v6.1.18
Docs & License: https://fullcalendar.io
(c) 2024 Adam Shaw
*/
(function (index_js) {
    'use strict';

    var locale = {
        code: 'en-au',
        week: {
            dow: 1,
            doy: 4, // The week that contains Jan 4th is the first week of the year.
        },
        buttonHints: {
            prev: 'Previous $0',
            next: 'Next $0',
            today: 'This $0',
        },
        viewHint: '$0 view',
        navLinkHint: 'Go to $0',
        moreLinkHint(eventCnt) {
            return `Show ${eventCnt} more event${eventCnt === 1 ? '' : 's'}`;
        },
    };

    index_js.globalLocales.push(locale);

})(FullCalendar);

insert into users(firstname, lastname, email, username, password_hash, created_at, updated_at, about_me, last_seen)
    values
    ('Hans', 'Gruber', 'hans.gruber@nakatomi.com', 'hans', '$6$rounds=656000$MjyyCNgD39HJrbnK$ijz6hNLIWDQPsQkM.aGkWBvvx5N6i3zD0gdPzfpeGz2RNO8xCw9MRPbjplk//OuI0qx1VQneLWnBQ.A2Xfup.0', NOW(), NOW(), 'i hate John McClane', NOW()),
    ('Simon', 'Gruber', 'simon.gruber@nyfr.com', 'simon', '$6$rounds=656000$OBUey4BeZjwQG2Yb$4LJrIexa.uU8dvswbW9B7lLy5XniCxQJlcEIMXUnEya6wx/Gq37/V6Z6hS5kNf2OidYBARkdjY7a3iMAaNh0Q0', NOW(), NOW(), 'Birds of a feather, flock together, so do pigs and swine. Rats and mice all have their chance, as will I have mine', NOW()),
    ('John', 'McClane', 'john.mcclane@nypd', 'johnboy', '$6$rounds=656000$KtgmndKI6o0JunCT$f3etnFgLbGR16jXWboWjwnfRF2gG6xxnBOLKHvNclbWgZEw2sCQjPjVkWMJLOevK2k.7/3huvgxTSgu2Py48B0', NOW(), NOW(), 'yippiekayay...', NOW()),
    ('Holly', 'Gennero', 'holly.gennero@nakatomi.com', 'holly', '$6$rounds=656000$10.6XScywDDO3AsT$oiwlxIdCKgtFUQ3sGJ.kELdMxaXgZrPJj8r718Gb5esmHsTRR81ZBnOQEIH5prYps6ZRWYOU1o0XoP3wNVTej/', NOW(), NOW(), null, null);

insert into followers(follower_id, followed_id)
    values
    (1, 2),
    (2, 1),
    (3, 1),
    (3, 2),
    (3, 4),
    (4, 3);

insert into posts(body, timestamp, user_id)
    values
    ('This time John Wayne does not walk off into the sunset with Grace Kelly.', '2018-05-05 10:00:00.000000+00', 1),
    ('That was Gary Cooper, a**hole.', '2018-05-05 10:01:00.000000+00', 3),
    ('And when Alexander saw the breadth of his domain, he wept, for there were no more worlds to conquer.', '2018-05-05 09:00:00.000000+00', 1),
    ('You asked for miracles, Theo, I give you the F.B.I.', '2018-05-05 11:00:00.000000+00', 1),
    ('Come out to the coast, we`ll get together, have a few laughs...', '2018-05-05 11:05:00.000000+00', 3),
    ('Welcome to the party, pal.', '2018-05-05 12:05:00.000000+00', 3),
    ('No code, no riddle, no fancy little countdown.', '2018-05-05 22:05:00.000000+00', 2),
    ('Simon`s going to tell Lt. McClane what to do, and Lt. McClane is going to do it. Noncompliance will result in a penalty.', '2018-05-05 22:15:00.000000+00', 2),
    ('What idiot put you in charge', '2018-05-05 13:00:00.000000+00', 1),
    ('You did', '2018-05-05 13:00:05.000000+00', 4);

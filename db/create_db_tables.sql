CREATE TABLE `info` (
  `lottery_id` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  `image` varchar(500) DEFAULT NULL
);

CREATE TABLE `numbers` (
  `id` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  `p` int(11) DEFAULT NULL,
  `n` int(11) DEFAULT NULL,
  `lottery_id` int(11) NOT NULL
);

ALTER TABLE `info`
  ADD PRIMARY KEY (`lottery_id`);

ALTER TABLE `numbers`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `numbers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

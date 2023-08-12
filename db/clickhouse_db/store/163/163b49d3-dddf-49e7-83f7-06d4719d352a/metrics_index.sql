ATTACH TABLE _ UUID 'd940b2fb-4b07-4a9d-92ce-bf385ce1980e'
(
    `Date` Date,
    `Level` UInt32,
    `Path` String,
    `Version` UInt32
)
ENGINE = ReplacingMergeTree(Version)
PARTITION BY toYYYYMM(Date)
ORDER BY (Level, Path, Date)
SETTINGS index_granularity = 8192

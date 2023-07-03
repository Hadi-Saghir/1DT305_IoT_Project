function Decoder(payload, port) {
  if (port === 1) {
    var temperature = payload.readInt16BE(0); // Read the temperature value as a signed 16-bit integer
    var humidity = payload.readUInt8(2); // Read the humidity value as an unsigned 8-bit integer
    var state = payload.toString('utf8', 3, 4); // Read the state value as a single character (UTF-8 encoded)

    return [
      {
        field: "TEMPERATURE",
        value: temperature
      },
      {
        field: "HUMIDITY",
        value: humidity
      },
      {
        field: "STATE",
        value: state === 'w' ? "warm" : "brew"
      }
    ];
  }
}
